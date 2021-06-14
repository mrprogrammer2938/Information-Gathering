#!/usr/bin/env bash
# This code write by Mr.nope
if [[ "$(id -u)" -ne 0 ]]; then
   echo ""
   echo "Please, Run This Programm as Root!"
   echo ""
   exit 1
fi
clear
printf '\033]2;Information Gathering\a'
echo "Installing..."
sleep 2
apt install python
apt install python3
chmod +x Information-Gathering.py
echo ""
echo "Installing..., Finish...!"
echo ""
exit 1
