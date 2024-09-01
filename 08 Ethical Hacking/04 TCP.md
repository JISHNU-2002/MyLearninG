- **TCP (Transmission Control Protocol)** is one of the core protocols of the Internet Protocol Suite, which is used for network communication\

![tcp](images/tcp.png)
### Key Features of TCP
1. **Connection-Oriented**
   - TCP establishes a connection between the sender and receiver before transmitting data
   - This is done through a process called the **three-way handshake**
   - The **three-way handshake** involves three steps
     1. **SYN**: The sender sends a synchronization (SYN) packet to the receiver
     2. **SYN-ACK**: The receiver responds with a synchronization acknowledgment (SYN-ACK) packet
     3. **ACK**: The sender acknowledges the receiver's response with an acknowledgment (ACK) packet

2. **Reliable Delivery**
   - TCP ensures that data is delivered accurately and in the correct order
   - It uses acknowledgments and sequence numbers to track and manage the data
   - If a packet is lost or corrupted, TCP will retransmit it

3. **Flow Control**
   - TCP uses flow control mechanisms to prevent a sender from overwhelming a receiver with too much data at once
   - It uses a sliding window technique to manage the amount of data in transit

4. **Congestion Control**
   - TCP adjusts the rate of data transmission based on network congestion
   - It uses algorithms like slow start, congestion avoidance, and congestion recovery to optimize data flow

5. **Error Checking**
   - TCP uses checksums to detect errors in transmitted data
   - If an error is detected, the affected packets are retransmitted

6. **Ordered Data Transfer**
   - TCP ensures that data is received in the same order it was sent
   - It achieves this by numbering packets and reassembling them at the receiver's end

### How TCP Works
1. **Connection Setup**
   - Before data can be sent, a connection is established using the three-way handshake.
   
2. **Data Transfer**
   - Data is transmitted in segments. Each segment includes a sequence number, acknowledgment number, and other control information.
   - The receiver sends acknowledgments for successfully received segments. If segments are missing or erroneous, the sender retransmits them.

3. **Connection Termination**
   - When data transmission is complete, the connection is terminated through a four-step process:
     1. **FIN**: One side sends a finish (FIN) packet indicating that it has finished sending data
     2. **ACK**: The other side acknowledges the FIN packet
     3. **FIN**: The second side sends its own FIN packet
     4. **ACK**: The first side acknowledges the second FIN packet

### Example Scenario
Imagine you're sending a large file from your computer to a friend's computer over the Internet. TCP would:

1. Establish a connection with your friend's computer
2. Break the file into smaller segments and send them
3. Ensure that each segment is received correctly and in the right order
4. Retransmit any segments that are lost or corrupted
5. Close the connection when the file transfer is complete