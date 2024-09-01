- A MAC address, or **Media Access Control address**, is a unique identifier assigned to network interfaces for communications on the physical network segment
- It operates at the Data Link Layer (Layer 2) of the OSI model and is used to uniquely identify devices on a network
- Unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment
- It's also known as a hardware ID number or physical address

![MAC](images/mac.png)

- **Format**
	-  A MAC address is typically represented as a 12-digit hexadecimal number, often displayed in six pairs separated by colons (e.g., `00:1A:2B:3C:4D:5E`) or hyphens (e.g., `00-1A-2B-3C-4D-5E`).

- **Uniqueness**
	- Each MAC address is supposed to be unique to the network interface card (NIC) it is assigned to
	- This uniqueness is maintained by the IEEE, which allocates MAC address ranges to hardware manufacturers

- **Purpose**
	- MAC addresses are used in network protocols to ensure that data packets are delivered to the correct device within a local network
	- They are essential for network management and security, helping to direct traffic and filter network access

1. **Device Identification** : MAC addresses help identify devices on a local network. This is crucial for network communication, as it ensures that data is sent to the correct device.
    
2. **Network Management** : Network administrators use MAC addresses to configure network switches, routers, and other devices. They can create access control lists (ACLs) or apply network policies based on MAC addresses.
    
3. **Security** : MAC addresses are used in security protocols to filter network access. For example, a router might be configured to allow only devices with specific MAC addresses to connect to the network.

- **Types**
	   - **Unicast** : Addresses that identify a single network interface
	   - **Broadcast** : A special MAC address (`FF:FF:FF:FF:FF:FF`) used to send packets to all devices on a local network
	   - **Multicast** : Addresses used to send packets to a group of devices

- **Static and Dynamic Addresses** : Generally, MAC addresses are fixed (hard-coded into hardware), but some devices allow users to change the MAC address through software, often for privacy reasons

