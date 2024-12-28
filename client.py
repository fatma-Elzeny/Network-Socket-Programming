import socket  

def main():
    # Mapping operations with server IPs and ports
    operations = {
        'add': ('10.145.18.188', 4000),  
        'sub': ('10.145.24.3', 3456), 
        'mul': ('10.145.24.4', 4567), 
        'div': ('10.145.24.5', 5678)  
    }

    
    operation = input("Enter operation (add, sub, mul, div): ").strip().lower()
    if operation not in operations:  
        print("Invalid operation.")  
        return

    try:
        
        operand1 = float(input("Enter operand 1: "))
        operand2 = float(input("Enter operand 2: "))
    except ValueError:  
        print("Invalid operands.")
        return

    # Get the server IP and port based on the chosen operation
    server_ip, server_port = operations[operation]

    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))  
        message = f"{operand1},{operand2}"  
        s.sendall(message.encode())  
        result = s.recv(1024).decode()  
        print(f"Result: {result}")  

# Entry point of the program
if __name__ == "__main__":
    main()