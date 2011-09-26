import time
import socket
import threading
import libs.threadmanager
import tunnels.base
import libs.events

class Tunnel(tunnels.base.Tunnel):
    '''Make a direct UDP connection to a peer'''
    pass
    
class Connection(tunnels.base.Connection):
    '''UDP "connection" to a peer'''
    def __init__(self, address, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((address, port))
        
        self.sock.send('Can I connect?\n')
    
class Listener(libs.threadmanager.Thread):
    '''Listen for UDP connections on our port'''
    def __init__(self, port = 1337):
        super(Listener, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.bind(('0.0.0.0', port)) # TODO: bind other addresses
        self.sock.setblocking(False)
        
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()
        
    def run(self):
        while not self._stop.isSet():
            try:
                data = self.sock.recvfrom(4096)
                msg = tunnels.base.Message(data[1][0], data[1][1], data[0])
                libs.events.broadcast('got_message', msg)
            except socket.error, error:
                if error.errno == 11: # No messages
                    time.sleep(1)       
        
        
def start():
    listener = Listener()
    listener.start()
    libs.threadmanager.register(listener)