#!/bin/sh

# Find the connection UUID with "nmcli connection show" in terminal.
# All NetworkManager connection types are supported: wireless, VPN, wired...
if [ "$2" = "up" ]; then
  if [ "$CONNECTION_UUID" = "put your uuid here" ]; then
    su USER -c /home/USER/duplicati-laptop-backup/duplicati-wifi-trigger.py > /home/USER/duplicati-laptop-backup/log &
  fi
fi
