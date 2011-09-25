'''This module manages events and evet handlers'''
event_handlers = []

def register_handler(handler):
    '''Register an event handler'''
    if isinstance(handler, Handler):
        event_handlers.append(handler)
    else:
        raise Exception('Object must be a subclass of libs.events.Handler')

def unregister_handler(handler):
    '''Unregister an event handler'''
    event_handlers.remove(handler)
    
def broadcast(event_type, *args):
    '''Broadcast and event to all handlers in `handlers`'''
    for handler in event_handlers:
        getattr(handler, event_type)(*args)

class Handler(object):
    '''Base handler class. Provides default methods to handle events. This must
    be used by all modules and is done to ensure compatibility.'''
    def got_message(self, message):
        '''Called when a message is recieved'''
        pass

    def got_connect(self, connection):
        '''Called when we get or establish a connection'''
        pass
        