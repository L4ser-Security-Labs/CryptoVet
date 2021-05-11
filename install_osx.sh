#!/bin/bash

brew update
brew install python3
sudo pip3 install virtualenv


cd ..
virtualenv venv
source venv/bin/activate
cd CryptoVet/
pip3 install -r requirements.txt
python3 CryptoVet.py