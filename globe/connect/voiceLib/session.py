class Session:
    # capture json when class is instantiated
    #
    # @param    string      json
    def __init__(self, json):
        self.obj = {}
        self.json = json
    
    # object getter
    #
    # return    object  obj
    def getObject(self):
        # check if session key is not set
        if 'session' not in self.json:
            # raise an exception
            raise Exception('Invalid json data')
        
        # store session values to obj
        self.obj = self.json['session']
        
        # set default values
        self.obj['to'] = ''
        self.obj['from'] = ''
        self.obj['headers'] = ''
        self.obj['parameters'] = ''
        
        # return obj
        return self.obj
