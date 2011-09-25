import socket
import tunnels.base

class Tunnel(tunnels.base.Tunnel):
    '''Make a direct UDP connection to a peer'''
    pass
    
class Connection(tunnels.base.Connection):
    '''UDP "connection" to a peer'''
    pass
    
class Listener(object):
    '''Listen for UDP connections on our port'''
    def __init__(self, port = 9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.bind(('0.0.0.0', port)) # TODO: bind other addresses