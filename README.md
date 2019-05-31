# duplicati-laptop-backup
Duplicati script I use to backup my laptop.

## Instructions
Your settings have to be added into the two files.

### 30-duplicati-wifi-trigger.sh
* Run `nmcli connection show` and replace 'put your uuid here' with the UUID you want to use.
* Replace '/home/USER/duplicati-laptop-backup/' the location of 'duplicati-wifi-trigger.py'.
* Place the file in '/etc/NetworkManager/dispatcher.d' and give it permissions 755, and set `root` as the owner.

### duplicati-wifi-trigger.py
* Fill out the 5 commented variables towards the beginning of the script: `duplicati_command`, `wait`, `directory`, `user` and `dispatch_directory`.
* Ensure the script is owned by the user specified in it, and that that user has execution privileges over it.
