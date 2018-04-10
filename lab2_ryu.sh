#!/usr/bin/env bash

cd ~/repos/ryu

ryu-manager --observe-links \
ryu/app/gui_topology/gui_topology.py \
ryu/app/simple_switch_websocket_13.py
