import socket
from config import *

class Client():
    def __init__(self, ip_address = ip_address,port_number=port_number):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip_address , port_number))
                
    def send_data(self,data_package):    
        self.client.sendall(data_package.encode())
        response = self.client.recv(1024)
        print(f"Received response from server: {response.decode()}")
        self.client.close()

if __name__ == "__main__":
    # my_str = "{[1, 2], 0}; {[1, 3], 1}; {[2, 2], 0}; {[2, 3], 0}"
    my_str = "this is not true"
    client1 = Client()
    client1.send_data(my_str)
    second_str="{[2, 1], 1}; {[2, 2], 1}; {[3, 1], 0}; {[3, 2], 0}"
    client2 = Client()
    client2.send_data(second_str)


