# SSH\_alert\_bot

### ::::: Description :::::
This bot notifies any access using SSH to your computer using the API from the LINE application.

### ::::: Initial setup :::::
1. make a directory "LINE\_bot/ssh\_alert" under /opt
2. move the "ssh\_alert\_bot.py" file under the /opt/LINE\_bot/ssh\_alert directory
3. move the "ssh\_alert\_bot.service" under "/etc/systemd/system" directory
4. get the token for the LINE API from the following link and paste the token to "access\_token" in the "ssh\_alert\_bot.py"
	- https://notify-bot.line.me
5. activate the daemon with the following command.
	- $ sudo systemctl enable ssh\_alert\_bot.service
	- $ sudo systemctl start ssh\_alert\_bot.service

### ::::: Updates :::::
