## RPM (Red Hat Package Manager)
---

- Manages software packages on Linux systems

- **Installation**
```bash
rpm -i package.rpm
```

- **Upgrade**
```bash
rpm -Uvh package.rpm
```

- **Querying Packages**
	- To find out information about an RPM package
	- Listing Files in an RPM
```bash
rpm -ql package
rpm -qlp package.rpm
rpm -qf /usr/bin/file
```

- **List Installed Packages**
```bash
rpm -qa
```

 - **Remove Packages**
```bash
rpm -e package
```

## yum (Yellowdog Updater Modified)
---

- Interactive, RPM-based package manager\
- It can automatically perform system updates, including dependency analysis and obsolete processing

- **Install a Package**
```bash
yum install package
```

- **Remove a Package**
```bash
yum remove package
```

- **Update a Package**
```bash
yum update package
```

- **List a Package**
```bash
yum list package
```

- **Search for a Package**
```bash
yum search package
```

- **Get Information on a Package**
```bash
yum info package
```

## APT (Advanced Package Tool)
---

- Manages Debian-based distributions like Ubuntu
- `apt-get` installing, upgrading, and cleaning packages
- `apt-cache` is used for finding new packages

- **Install a Package**
```bash
sudo apt-get install package
```

- **Update Package Database**
	- `hit`  no change in the package version
	- `ign` the package is being ignored
	- `get` new version of the package available
```bash
sudo apt-get update
```

- **Upgrade Packages**
```bash
sudo apt-get upgrade
```

- **Search for a Package**
```bash
apt-cache search package
```

- **Show Package Info**
```bash
apt-cache show package
```

- **Remove a Package**
```bash
sudo apt-get remove package
sudo apt-get purge package
sudo apt-get clean
sudo apt-get autoclean
```


### apt-get vs apt
- `apt` is more structured 
- Provides necessary options needed to manage packages

```bash
apt help
sudo apt install glances
sudo apt content glances
sudo apt depends glances
sudo apt search apache2
sudo apt show firefox
sudo apt check firefox
sudo apt version firefox
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt autoclean
sudo apt clean
sudo apt purge glances
```