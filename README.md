# Network-Socket-Programming
 the server and client Python socket programs to work between two different laptops , you need to use the actual IP addresse of the server(10.145.18.188) in our case. Additionally, you'll need to ensure that the server is listening on the network interface and that firewall settings allow the communication between the two laptops.

### Steps for Running the Server and Client on Two Different Laptops:

1. **Find the IP address of the server laptop**:
   On the **server laptop**, you can find the IP address by running:
   ```bash
   ifconfig
   ```
   or:
   ```bash
   ip addr
   ```
   Look for the `inet` address under the active network interface (e.g., `eth0`, `wlan0`).



2. **Modify the Server Script**:
   On the **server laptop**, use the IP address you obtained instead of `10.145.18.188` (localhost).

### 1. **Server-Side (Listening for Connections)**

### 2. **Client-Side (Connecting to Server)**

On the **client laptop**, modify the client code to connect to the server's IP address:

### 3. **Running the Server and Client on Different Laptops**

1. **Run the Server**:
   - On the **server laptop**, open a terminal and start the server by running:
   ```bash
   python3 server.py
   ```

2. **Run the Client**:
   - On the **client laptop**, open a terminal and start the client by running:
   ```bash
   python3 client.py
   ```


### Notes:
- Ensure the **firewall** on both laptops allows traffic on port `4000`. You may need to open the port on the server using `ufw` or another firewall tool if it’s restricted.
- **Network Configuration**: Both laptops need to be on the same network (e.g., connected to the same Wi-Fi) for this setup to work.
- **IP Address Configuration**: If you're using dynamic IP addresses, the IP of the server may change, so you may need to adjust the IP in the client code accordingly.


