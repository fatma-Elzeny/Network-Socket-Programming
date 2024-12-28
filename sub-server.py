import socket 
# Function to handle client requests
def handle_client(conn):
    data = conn.recv(1024).decode()  # Receive data from the client
    operand1, operand2 = map(float, data.split(","))  # Extract operands
    result = operand1 - operand2  # Perform addition
    conn.sendall(str(result).encode())  # Send the result back to the client

def main():
    # Create a socket object for TCP communication
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('10.145.18.188', 4000))  # Bind to the specified IP and port
        server.listen()  # Listen for incoming connections #you can specify How many client to connect 
        print("Add Server is running...")  # Inform that the server is running
        while True:
            conn, _ = server.accept()  # Accept a new connection
            with conn:  # Ensure proper closure of the connection
                handle_client(conn)  # Process the client request

# Entry point of the program
if __name__ == "__main__":
    main()
