import socket
import libs.threadmanager

class UI(libs.threadmanager.Thread):
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('localhost', 6667))
        self.sock.setblocking(False)
        
    def run(self):
        while not self._stop.isSet():
            try:
                data = self.sock.recvfrom(4096)
                msg = tunnels.base.Message(data[1][0], data[1][1], data[0])
            except socket.error, error:
                if error.errno == 11: # No messages
                    time.sleep(1)
    
    def got_message(self, id, message):
        '''Send a message to the IRC client'''
        pass