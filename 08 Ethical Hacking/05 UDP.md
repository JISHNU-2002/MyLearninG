- **UDP (User Datagram Protocol)** is one of the core protocols of the Internet Protocol (IP) suite
- It is used for transmitting data over a network and is known for its simplicity and speed

![udp](images/udp.png)
### Key Features

- **Connectionless**
	- UDP does not establish a connection before sending data
	- It simply sends packets (called datagrams) to the destination without any handshake process
	- This makes it faster but less reliable compared to connection-oriented protocols like TCP

- **Unreliable**
	- UDP does not guarantee the delivery of packets
	- There is no acknowledgment of receipt, and packets may be lost or arrive out of order
	- It's up to the application to handle any necessary error checking and recovery

- **No Flow Control**
	- UDP does not have mechanisms for flow control or congestion control
	- This means that if the sender is faster than the receiver, packets may be dropped without any mechanism to manage this

- **Low Overhead**
	- Because UDP has minimal overhead (no connection setup, no acknowledgment, and no flow control), it is often used in situations where speed is crucial and the application can tolerate some level of data loss

- **Data is Sent in Packets**
	- Data is divided into small chunks called **datagrams**
	- Each datagram is independent of others, and the receiver processes each datagram separately

### Use Cases
UDP is often used in applications where speed and efficiency are more important than reliability

- **Streaming Media** : Video and audio streaming where occasional data loss is acceptable
- **Online Gaming** : Where real-time performance is critical, and occasional packet loss can be tolerated
- **DNS Queries** : Domain Name System (DNS) queries use UDP because they are typically short and a few lost queries can be retried

### Example
```python
# UDP Server
import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received message: {data.decode()} from {addr}")

# UDP Client
import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, UDP!"
    client_socket.sendto(message.encode(), ('localhost', 12345))
    print("Message sent!")

# Uncomment these lines to run the server and client
# udp_server()
# udp_client()
```

