#!/usr/bin/env bash 

# controller "floodlight" installation
# prerequisite
sudo apt-get update
sudo apt-get install build-essential default-jdk ant python-dev eclipse git
cd ~

if [ -d "repos" ]; then
  cd repos
else
  mkdir repos && cd repos
fi

git clone https://github.com/floodlight/floodlight
cd floodlight
git submodule init
git submodule update
ant
sudo mkdir /var/lib/floodlight
sudo chmod 777 /var/lib/floodlight
# Mininet installation
cd ../
git clone https://github.com/mininet/mininet.git
./mininet/util/install.sh -a
