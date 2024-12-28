import socket 

def handle_client(conn):
    data = conn.recv(1024).decode()  
    operand1, operand2 = map(float, data.split(","))  
    result = operand1 / operand2  
    conn.sendall(str(result).encode())  

def main():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('10.145.24.5', 5678))  
        server.listen()  
        print("Add Server is running...")  
        while True:
            conn, _ = server.accept()  
            with conn:  
                handle_client(conn)  


if __name__ == "__main__":
    main()