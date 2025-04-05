# import socket

# class Network:
#     def __init__(self):
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server = "192.168.100.23"  # Replace with your server IP
#         self.port = 5555
#         self.addr = (self.server, self.port)
#         self.pos = self.connect()
#         print("Connected to server with ID:", self.pos)

#     def getPos(self):
#         return self.pos
    
    
#     def connect(self):
#         try:
#             self.client.connect(self.addr)
#             return self.client.recv(2048).decode('utf-8')  # Added proper decoding
#         except socket.error as e:
#             print(f"Connection error: {e}")
#             return None
        
        
#     def send(self, data):
#         try:
#             self.client.send(str.encode(data))  # Ensure data is encoded
#             return self.client.recv(2048).decode('utf-8') # Added proper
#         except socket.error as e:
#             print(f"Send error: {e}")
#             return None    
        
          
#     def close(self):  # Added close method for proper cleanup
#         self.client.close()


import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.100.23"  # Replace with your server IP
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        print("Connected to server with ID:", self.pos)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(f"Connection error: {e}")
            return None

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(f"Send error: {e}")
            return None

    def close(self):
        self.client.close()
