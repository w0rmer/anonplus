import libs.events
OUTPUT = True

class Logger(libs.events.Handler):
    '''Print events as they happen. TODO: Write to a log file'''
    def got_message(self, message):
        self._output('Got a message')

    def got_connect(self, connection):
        self._output('Got a connection')

    def _output(self, message):
        print('[*] %s' % message)

if OUTPUT:
    logger = Logger()
    libs.events.register_handler(logger)