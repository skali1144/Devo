#!/bin/bash
"Running devo.sh..."
" if it asks for your password write the password of your login system."
sleep 5
sudo apt update
sudo apt upgrade
sudo apt install kali-linux-everything
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew upgrade
brew install metasploit
brew install wireshark
brew install hydra
brew install wifite
brew install nano
brew install nmap
brew install aircrack-ng
