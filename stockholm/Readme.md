# Stockholm

## Project Overview

Stockholm is a Python-based file encryption and decryption tool designed for securing files within a designated directory. It uses the Fernet encryption from the cryptography library and supports reversing the encryption process. The project includes Docker support for containerized execution.

## Features

- **Encrypt Files**: Secures files in a specified directory with Fernet encryption.
- **Decrypt Files**: Reverses encryption using the generated key.
- **Silent Mode**: Suppresses output for seamless automation.
- **File Compatibility**: Targets various file types via extensions list.
- **Docker Support**: Provides easy deployment and testing.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```
Navigate to the project directory:

```bash
cd stockholm
```
Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage

Run the script using the following commands:

Encrypt files:

```bash
stockholm
```
Decrypt files:

```bash
stockholm -r
```
Silent mode:

```bash
stockholm -s
```
Docker

Build and run the Docker image:

```bash
docker build -t stockholm .
docker run -it --rm -v $(pwd):/app stockholm
```
