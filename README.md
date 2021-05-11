# CryptoVet v1.0

![CryptoVet Banner](https://i.imgur.com/MhZjWV1.png)

CryptoVet is a command-line Crypto audit and threat intelligence tool.

## Features

- **General Information Check**: See general information about a specified wallet address.
  
- **Transactions Check**: View all incoming and out going transactions for the specified wallet address.
  
- **Abuse Check**: Check if a wallet address has been reported for scam/fraudulent activities by malicious parties and retrive informotion about the abuse.
  
- **Report Abuse**: For a given wallet address, report it as a fradulent/scam addressed used by malicious parties.
  
## Installation

CryptoVet requires [Python 3](https://www.python.org/download/releases/3.0/)+ to run.

```sh
Using Python Virtual Environment
$ git clone https://github.com/L4ser-Security-Labs/CryptoVet.git
$ cd CryptoVet/
$ sh install_osx.sh
$ sh install_linux.sh

or

Using Docker Image
$ git clone https://github.com/L4ser-Security-Labs/CryptoVet.git
$ sudo docker build -t "app" ./CryptoVet
$ sudo docker run -i app
```

### Use cases

- **Threat Intelligence Analysis for Investigators**
Find detailed information about a wallet address in seconds.

### Change Log

- 1.0 Initial Release

### Todos

- Support more crypto coins
- Add more sources
- Integration of other Open Source security tools

**Free Tool, Hell Yeah!**
