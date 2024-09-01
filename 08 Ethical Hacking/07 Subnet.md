### **Subnetting Overview**
- Subnetting is the process of dividing a large network into smaller, more manageable sub-networks, or subnets
- This is done by manipulating the subnet mask, which determines how an IP address is split between the network and the host portion

### **IP Address Structure**
- An IP address is a 32-bit number, usually represented in decimal form as four octets separated by periods (e.g., 192.168.1.1)
- Each octet represents 8 bits of the address, and the entire IP address is split into two parts:
1. **Network Portion :** Identifies the network
2. **Host Portion :** Identifies a device within that network

### **Subnet Mask**
- A subnet mask is a 32-bit number that masks an IP address and divides the IP address into the network and host portions
- It also determines how many subnets and hosts per subnet can be created
**Example Subnet Mask**
- **255.255.255.0** : This is a common subnet mask for a Class C network. It means that the first three octets (24 bits) are the network portion, and the last octet (8 bits) is the host portion.

### **Subnetting Process**
- Let's say you have an IP address **192.168.1.0/24** and you want to divide this into smaller subnets
- The `/24` means that 24 bits are used for the network portion, leaving 8 bits for the host portion

#### **Example: Creating 4 Subnets**
1. **Determine the Number of Subnets**
   - You want 4 subnets. To find out how many bits you need to borrow from the host portion, use the formula
     $\(2^n \geq \text{{Number of Subnets}}\)$  
     \(2^2 = 4\), so you need to borrow 2 bits
 - **Subnetting** allows more efficient use of IP addresses by dividing a network into smaller subnets
- **Borrowing Bits** from the host portion creates additional subnets but reduces the number of available hosts per subnet

2. **Calculate the New Subnet Mask**
   - Original subnet mask: **255.255.255.0** (/24)
   - New subnet mask: Borrow 2 bits from the host portion:
     - **11111111.11111111.11111111.11000000** (binary)
     - **255.255.255.192** (/26)

3. **Determine the Subnet IP Ranges**
   - With a /26 subnet mask, each subnet will have 64 IP addresses (2^6 = 64). The subnets would be:
     1. **192.168.1.0/26**: Range: 192.168.1.0 - 192.168.1.63
     2. **192.168.1.64/26**: Range: 192.168.1.64 - 192.168.1.127
     3. **192.168.1.128/26**: Range: 192.168.1.128 - 192.168.1.191
     4. **192.168.1.192/26**: Range: 192.168.1.192 - 192.168.1.255
![subnet](images/subnet.png)
4. **Calculate Usable IP Addresses**
   - In each subnet, the first IP is the network address, and the last IP is the broadcast address, so the usable IP range is:
     - **192.168.1.1 - 192.168.1.62** (for the first subnet)
     - **192.168.1.65 - 192.168.1.126** (for the second subnet)
     - **192.168.1.129 - 192.168.1.190** (for the third subnet)
     - **192.168.1.193 - 192.168.1.254** (for the fourth subnet)
- This approach helps in managing and utilizing IP address spaces efficiently, especially in large networks


### **How Subnet Masks Work with IP Addresses**
When you apply a subnet mask to an IP address:

1. **AND Operation** 
   - The subnet mask is applied to the IP address using a bitwise AND operation
   - This operation helps to extract the network portion of the IP address
   - **Example:**
     - IP Address: `192.168.1.10` → `11000000.10101000.00000001.00001010` (binary)
     - Subnet Mask: `255.255.255.0` → `11111111.11111111.11111111.00000000` (binary)
     - Result (Network Address): `11000000.10101000.00000001.00000000` → `192.168.1.0`

2. **Verification of Network Membership**
   - If you need to check whether two IP addresses are in the same subnet, you would apply the subnet mask to both IP addresses
   - If the resulting network addresses are the same, the IPs are in the same subnet

