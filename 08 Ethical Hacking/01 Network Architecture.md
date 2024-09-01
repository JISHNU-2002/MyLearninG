# OSI Model
- The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and implement network protocols in seven distinct layers
- Each layer serves a specific function and interacts with the layers directly above and below it
- **OSI Model**
	- 1 Physical - data cables, cat6
	- 2 Datalink - switching, MAC addresses
	- 3 N/W - IP, routing
	- 4 Transport - TCP/UDP
	- 5 Session - session management
	- 6 Presentation - WMV, JPEG, MOV
	- 7 Application - HTTP, SMTP

![osi_model](images/osi_model.gif)
### 1. **Physical Layer (Layer 1)**
   - **Function:** Responsible for the transmission and reception of raw bitstreams over a physical medium (e.g., cables, switches).
   - **Data Unit:** Bits
   - **Devices:** Hubs, cables, and repeaters
   - **Protocols:** Ethernet (at the physical level), RS-232

### 2. **Data Link Layer (Layer 2)**
   - **Function:** Provides node-to-node data transfer—a link between two directly connected nodes. It also handles error detection and correction from the physical layer.
   - **Data Unit:** Frames
   - **Devices:** Switches, bridges
   - **Sub-layers:**
     - **MAC (Media Access Control):** Controls how devices in a network gain access to a medium and permission to transmit data.
     - **LLC (Logical Link Control):** Handles error checking and frame synchronization.
   - **Protocols:** Ethernet, PPP (Point-to-Point Protocol), HDLC (High-Level Data Link Control)

### 3. **Network Layer (Layer 3)**
   - **Function:** Manages the routing of data between devices across different networks and handles packet forwarding including routing through different routers.
   - **Data Unit:** Packets
   - **Devices:** Routers
   - **Protocols:** IP (Internet Protocol), ICMP (Internet Control Message Protocol), ARP (Address Resolution Protocol)

### 4. **Transport Layer (Layer 4)**
   - **Function:** Provides reliable data transfer services to the upper layers. It ensures complete data transfer with error checking and recovery. It also manages flow control and data segmentation.
   - **Data Unit:** Segments (TCP), Datagrams (UDP)
   - **Devices:** Gateways, firewalls (at a basic level)
   - **Protocols:** TCP (Transmission Control Protocol), UDP (User Datagram Protocol)

### 5. **Session Layer (Layer 5)**
   - **Function:** Manages sessions or connections between two applications. It establishes, maintains, and terminates connections. It also handles session checkpointing and recovery.
   - **Data Unit:** Data
   - **Protocols:** NetBIOS, PPTP (Point-to-Point Tunneling Protocol)

### 6. **Presentation Layer (Layer 6)**
   - **Function:** Ensures that data is in a usable format and is where data encryption occurs. It translates data between the application layer and the network format.
   - **Data Unit:** Data
   - **Functions:** Data translation, encryption/decryption, data compression
   - **Protocols:** SSL/TLS (Secure Sockets Layer/Transport Layer Security), JPEG, MPEG

### 7. **Application Layer (Layer 7)**
   - **Function:** The closest layer to the end-user, it interacts with software applications that implement a communicating component. It provides services such as email, file transfer, and network resource sharing.
   - **Data Unit:** Data
   - **Protocols:** HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol), DNS (Domain Name System)

![osi_layers](images/osi_layers.jpg)

- Other network architectures
### 1. **TCP/IP Model**

![tcp/ip](images/tcp_layers.jpeg)
   - **Description:** The TCP/IP (Transmission Control Protocol/Internet Protocol) model is a more practical and widely used framework compared to the OSI model. It was developed to standardize the way data is transmitted over the internet and is the foundation of the modern internet.
   - **Layers:**
     1. **Network Interface Layer:** Corresponds to the OSI's Physical and Data Link layers. Handles the physical network hardware and protocols for data transmission.
     2. **Internet Layer:** Maps to the OSI's Network layer. Manages packet routing and addressing (e.g., IP).
     3. **Transport Layer:** Maps to the OSI's Transport layer. Provides end-to-end communication services (e.g., TCP and UDP).
     4. **Application Layer:** Covers OSI's Session, Presentation, and Application layers. Handles application-level protocols and data handling (e.g., HTTP, FTP, SMTP).
![tcp/ip vs osi](images/tcp_model.jpeg)
### 2. **Hybrid Model**

![hybrid](images/hybrid_model.jpeg)
   - **Description:** A combination of the OSI and TCP/IP models, often used to leverage the strengths of both. It applies the OSI model’s detailed layer structure while incorporating the practical aspects of the TCP/IP model.
   - **Example:** The TCP/IP model’s Application layer can be mapped to OSI’s Application, Presentation, and Session layers, while TCP/IP’s Network Interface layer maps to OSI’s Physical and Data Link layers.
![hybrid](images/hybrid.webp)

### 3. **Internet Architecture**

![internet](images/internet.png)
   - **Description:** Refers to the actual structure of the internet, focusing on how various components like routers, switches, and servers interact with one another to facilitate communication.
   - **Components:**
     - **Core Network:** High-capacity backbone that connects large networks and data centers.
     - **Edge Network:** Connects end-user devices to the core network, involving ISPs and local networks.
     - **Access Networks:** Local networks that connect end devices to the internet (e.g., Wi-Fi, Ethernet).

### 4. **Client-Server Model**

![client_sever](images/client_server.png)
   - **Description:** A network architecture where one machine (the client) requests services or resources from another machine (the server).
   - **Characteristics:**
     - **Clients:** End-user devices or applications requesting resources.
     - **Servers:** Provide resources or services to clients (e.g., web servers, database servers).

### 5. **Peer-to-Peer (P2P) Model**

![p2p](images/p2p.png)
   - **Description:** A decentralized network architecture where each device (peer) can act as both a client and a server, sharing resources directly with other peers without requiring a central server.
   - **Characteristics:**
     - **Decentralized:** No central authority, with peers communicating directly.
     - **Scalable:** Suitable for file-sharing networks and collaborative applications (e.g., BitTorrent).

