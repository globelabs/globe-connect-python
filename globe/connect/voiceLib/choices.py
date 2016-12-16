import json

class Choices:
    # capture value when class is instatiated
    #
    # @param    string  value
    def __init__(self, value):
        self.obj = {}
        if value is not None
            self.obj['value'] = value
    
    # mode setter
    #
    # @param    string      mode
    # @return   instance    self
    def setMode(self, mode):
        self.obj['mode'] = mode
        return self

    # terminator setter
    #
    # @param    string      terminator
    # @return   instance    self
    def setTerminator(self, terminator):
        self.obj['terminator'] = terminator
        return self
    
    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # loop in stored obj
        for key in self.obj:
            try:
                # try if obj has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if value is not set
        if 'value' not in self.obj:
            # raise an exception
            raise Exception('Choices value is required')
        
        # return obj
        return self.obj;

