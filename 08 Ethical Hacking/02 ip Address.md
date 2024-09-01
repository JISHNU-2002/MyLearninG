- An IP address (Internet Protocol address) is a unique identifier assigned to each device connected to a network that uses the Internet Protocol for communication
- It serves two main purposes : identifying the host or network interface and providing the location of the host in the network

### Types of IP Addresses
#### **IPv4 (Internet Protocol version 4)**
   - **Format:** IPv4 addresses are 32-bit numbers, typically represented in decimal format as four octets separated by periods (e.g., `192.168.1.1`)
   - **Range:** 0.0.0.0 to 255.255.255.255
   - **Example:** `192.168.0.1`
![ip](images/ip.png)

![ipa](images/ipa.webp)
#### **IPv6 (Internet Protocol version 6)**
   - **Format:** IPv6 addresses are 128-bit numbers, represented in hexadecimal format and separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`)
   - **Range:** 340 undecillion addresses, allowing for virtually limitless devices
   - **Example:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

### IP Address Components
1. **Network Portion :** Identifies the specific network. The size of this portion depends on the subnet mask.
2. **Host Portion :** Identifies the specific device (or host) within the network.

### Subnet Mask
- A subnet mask defines which portion of an IP address is the network part and which is the host part.
- Example: For an IP address `192.168.1.1` with a subnet mask `255.255.255.0`, the first three octets (`192.168.1`) represent the network, and the last octet (`1`) identifies the specific device on that network.

### Public vs. Private IP Addresses
1. **Public IP Address:**
   - Used for devices on the global internet.
   - Must be unique across the entire internet.
   - Example: `8.8.8.8` (Google's public DNS server)

2. **Private IP Address:**
   - Used within private networks (e.g., home or corporate networks).
   - Not routable on the internet but can communicate within the local network.
   - Common ranges:
     - `10.0.0.0` to `10.255.255.255`
     - `172.16.0.0` to `172.31.255.255`
     - `192.168.0.0` to `192.168.255.255`
   - Example: `192.168.1.1`

### Dynamic vs. Static IP Addresses

1. **Static IP Address:**
   - Manually assigned and remains constant.
   - Often used for servers and other critical devices that need a consistent address.

2. **Dynamic IP Address:**
   - Automatically assigned by a DHCP (Dynamic Host Configuration Protocol) server.
   - Can change over time, typically used for general-purpose devices like laptops and smartphones.

### How IP Addresses Work
- When a device wants to communicate with another device on a network, it uses the destination device's IP address to route the data.
- Routers use IP addresses to determine the best path to forward packets to their destination.

### Example Scenario
Let's say you want to visit a website. Here's a simplified process
1. **Your device** sends a request to a DNS server to translate the domain name (like `www.example.com`) into its corresponding IP address.
2. **Your device** then sends a request to the website's IP address.
3. **The website's server** responds to your device, allowing the content to be displayed in your browser.
