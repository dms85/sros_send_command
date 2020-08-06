# sros_send_command
Send Command and Get the Output from Nokia/Alcatel SROS through Jump Host

Send Command and get output to Nokia/Alcatel SROS via Jump Server

PC --- VPN --- (extenal IP)[Jump Host](internal IP) --- Internal Cloud ? --- Target Node

- Versions,
	- python : 3.7
	- paramiko : 2.7.1
	- Netmiko : 3.2.0
- Not designed to exit the program when target Node or Jump Host is unreachable
	- If target node is down/not reachable, or using wrong user/password will return 'Exit 5' and continue to the next target node
	- If unable to connect to Jump Host due to any reasons, will return 'Exit 3'
- Logging will be stored in predefined logfile.txt
- Tested on SROS 12 - 16
- Target node must using the same user/passwd
- Output format : dictionary [ip[command[output]]
- On some scenario, Jump Server has two interfaces
	- External IP for VPN connectivity
	- Internal IP to reach target node
	- In case only one interface exist, set internal IP = external IP
- Not tested, but can try to use for another platform by changing the target model
