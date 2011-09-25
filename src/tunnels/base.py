class Tunnel(object):
    '''Base Tunnel class. Should be subclassed by other tunnels for
    compatibility reasons as well as ease of use.
    '''
    def connect(self, address, port):
        '''Use this tunnel to connect to `address`:`port`'''
        pass

    def disconnect(self, nodeid):
        '''Disconnect from a node at `nodeid`'''
        pass

    def transfer(

class Connection(object):
    '''A class to store a connection to a peer'''
    pass
