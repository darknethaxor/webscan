#!/bin/bash
echo ""
apt update
apt upgrade -y
apt install git -y
apt install python -y
apt install python2 -y
pip install requests
pip install colorama
apt install php -y
clear
rm -rf $HOME/index.php
cp index.php $HOME
chmod +x *
bash webscan.sh
