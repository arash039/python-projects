# Inquisitor

Inquisitor is a Python tool designed for advanced network analysis and monitoring. Leveraging libraries like Scapy, it allows users to spoof ARP packets, and intercept and analyze network traffic in real-time.

## Usage

Repository includes an example use case environment made with docker containers and a Makefile for easier use. 
First build and run the containers:
```sh
make
```
Then give necessary permissions to docker volumes to operate:
```sh
make perm
```
Now the test environment is ready to use. To get the necessary information run:
```sh
make info
```
The Filezilla service would be accessible on the following and necessary credentials are ftpuser, ftppass:
```
http://localhost:5600
```
To do the ARP poisoning first get the sample command to run:
```sh
make run
```
then enter the inquisitor container and run the command above. Use -v command for verbose mode if needed:
```sh
make inquisitor
./inquisitor.py [SRC_IP] [SRC_MAC] [TARGET_IP] [TARGET_MAC]
```
finally to check if the ARP poisoning happened you can enter either the server or client and run this command:
```sh
make server
arp -n
```
To check wether monitoring happens for http, imap, ... use curl_app. First enter the app and then run a sample curl command, then check if the inquisitor catch it:
```sh
make curl_app
curl http://[SERVER_IP]:21
```
