#!/usr/bin/env bash
set -e
TARGET="none"

if [ $# -eq 0 ];then
  echo "Usage: ./lab2_env.sh [-h|--help] [-t|--target ovs|ryu|all]"
fi

while [[ $# -gt 0 ]];do
  key="$1"
  case $key in
    "-h"|"--help")
    echo "Usage: ./lab2_env.sh [-h|--help] [-t|--target ovs|ryu|all]"
    shift
    ;;
    "-t"|"--target")
    TARGET="$2"
    sudo apt-get update
    shift
    shift
    ;;
    *)
    # Do nothing
    shift
    ;;
  esac
done

if [ $TARGET == "ovs" ] || [ $TARGET == "all" ];then
  sudo apt-get install git autoconf automake libtool -y
  cd ~
  if [ -d "repos" ];then
    cd repos
  else
    mkdir repos && cd repos
  fi
  # Get & install Open vSwitch
  git clone https://github.com/openvswitch/ovs.git
  cd ovs
  git checkout v2.5.4
  ./boot.sh && ./configure
  make && sudo make install
  # Load & initilize the kernel module
  sudo /sbin/modprobe openvswitch
  sudo mkdir -p /usr/local/etc/openvswitch
  sudo ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema
  # Run up the daemon
  /bin/bash lab2_ovs.sh
fi

if [ $TARGET == "ryu" ] || [ $TARGET == "all" ];then
  sudo apt-get install python-pip git -y
  cd ~
  if [ -d "repos" ];then
    cd repos
  else
    mkdir repos && cd repos
  fi
  git clone git://github.com/osrg/ryu.git && cd ryu
  pip install .
fi
