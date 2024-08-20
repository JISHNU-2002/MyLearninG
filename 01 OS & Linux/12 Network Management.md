### Basic Linux Commands & Examples
---

### `su` 
- Substitute User / Switch User
- Switch user or become superuser during a login session

  ```bash
su - sanjay
```
### `sudo`
- Super User DO
- Provides administrative access without sharing the root password
- Example : Precede an admin command with `sudo`

### Configuring `sudo` Access
1. Log in as root
2. Create a user with `useradd`
3. Set a password with `passwd`
4. Edit `/etc/sudoers` with `visudo`
5. Enable sudo for the wheel group by uncommenting the line in the file
6. Save changes and exit

### Mounting File Systems
- Mount syntax : `mount -t type device mount-point`
- View mounted partitions : `mount`

```bash
mount -t vfat /dev/hda1 /mnt
```

### `dmesg`
- Viewing Kernel Logs
- List loaded drivers : `dmesg`
- Clear buffer logs : `dmesg -c`
- Use with text-manipulation tools : `dmesg | grep sda`

### Linux Network Configuration and Troubleshooting Commands
---

#### `ifconfig`
- Interface Configurator
- Initialize interface, assign IP, enable/disable interface

```bash 
ifconfig eth0 192.168.50.5 netmask 255.255.255.0
```

#### `ping`
- Packet INternet Groper
- Test connectivity using ICMP ( Internet Control Message Protocol )
- `-c` to limit requests

```bash
ping www.google.com
ping -c 5 www.google.com
```

#### `netstat`
- Network Statistic
- Display connection info, routing table

```bash
netstat -r
```

#### `hostname`
- Identify the system in a network
- Set permanently in `/etc/sysconfig/network`

#### `host`
- Find name to IP or IP to name in IPv4 or IPv6 and also query DNS records
- Query DNS records with `-t` option to find out DNS Resource Records like CNAME, NS, MX, SOA

```bash
host wwww.google.com
host -t CNAME www.redhat.com
```

#### `uname`
- Print system information
- `-a` print all information
- `-s` kernel-name
- `-n` network node hostname
- `-r` kernel-release 
- `-v` kernel-version
- `-m` machine hardware name
- `-p` processor : print the processor type or "unknown"
- `-i` hardware-platform

#### `telnet`
- Connect to a remote Linux computer

```bash
telnet hostname
telnet ip-address
```

#### `ssh`
- Secured Shell
- Securely connect to a remote computer

```bash
ssh user@hostname
```

#### `scp`
- Secure Copy
- Copy files between hosts securely on a n/w
- Use ssh for data transfer

```bash
scp -r SourceDirectory/ user@hostname:/path/

```

### Tools
---

#### `putty`
- PuTTY is a terminal emulator application which can act as a client for the SSH, Telnet, rlogin, and raw TCP
- Stores hosts and preferences
- Control over the SSH encryption key and protocol version
- IPv6 support

#### `winscp`
- Windows Secure Copy
- Open-source SecureFTP client for Windows
- Secure file transfers between local and remote server
- Uses SSH for security
