# HOTP Generator

This is a simple implementation of an HMAC-based One-Time Password (HOTP) generator in Python. The script allows you to securely store a key and generate one-time passwords based on a counter value.

## Features

- **Key Encryption**: Encrypts and decrypts the HOTP key using AES-256-GCM.
- **One-Time Password Generation**: Generates a 6-digit HOTP based on the current counter value.

## Dependencies

- Python 3
- PyCryptodome: Install using `pip install pycryptodome`

## Usage

### Store a Key

To store a key, use the `-g` option followed by the filename containing a 64-character hexadecimal key:

```sh
ft_otp -g <filename>
```
### Generate an OTP
To generate an OTP, use the -k option followed by the filename containing the encrypted key:

```sh
ft_otp -k ft_otp.key
```
