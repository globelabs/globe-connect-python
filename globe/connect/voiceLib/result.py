import json

class Result:
    # capture json when class is instantiated
    #
    # @param    string      json
    def __init__(self, json):
        self.obj = {}
        self.json = json
    
    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # check if result key exist
        if 'result' not in self.json:
            # raise an exception if not
            raise Exception('Invalid json data')
        
        # return values on result key
        return self.json['result']

