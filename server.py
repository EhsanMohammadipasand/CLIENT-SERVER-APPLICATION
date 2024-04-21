import socket
from config import *
import ast
import json

class Server:
    occupancy_data = [[0 for i in range(occupancy_data_dimension)] for j in range(occupancy_data_dimension)]
    def __init__(self,ip_address=ip_address,port_number=port_number):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip_address, port_number))
        print(port_number)
        self.server.listen(concurrent_connections)
        
    def handle_client(self,client_socket, address):
        print(f"Accepted connection from {address}")
        data = client_socket.recv(1024).decode()    
        try:   
            data = data.split(";")
            for package in data:
                temp = package.strip("{}")
                if "{" in temp:
                    temp = temp.strip(" {")
                temp=temp.split("]")
                occupancy=int(temp[1].strip(", "))
                location=temp[0]+str("]")
                location = ast.literal_eval(location)
                Server.occupancy_data[location[0]][location[1]] =occupancy
        except:
            message = "the data format you sent is not correct"  
            message = json.dumps(message).encode()
            client_socket.sendall(message)
            print(f"Connection from {address} closed")
            client_socket.close()
            return

        data_json = json.dumps(Server.occupancy_data).encode()
        # Echo back the received data
        client_socket.sendall(data_json)
        print(f"Connection from {address} closed")
        client_socket.close()

    def start_server(self):
        print("Server started. Listening on port 8888...")
        while True:
            client_socket, address = self.server.accept()
            self.handle_client(client_socket,address)
            client_socket.close()

if __name__ == "__main__":
    server = Server()
    server.start_server()    
    print()       


