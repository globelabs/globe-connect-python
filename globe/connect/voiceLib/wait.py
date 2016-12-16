class Wait:
    # capture mlscd when class is instantiated
    #
    # @param    string  mlscd
    def __init__(self, mlscd):
        self.obj = {}
        self.obj['milliseconds'] = mlscd
    
    
    # allowSignals setter
    #
    # @param    string      allow
    # @return   instance    self
    def allowSignals(self, allow):
        self.obj['allowSignals'] = allow
        return self
    
    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # loop in stored objects
        for key in self.obj:
            try:
                # try if object has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if milliseconds is not set
        if 'milliseconds' not in self.obj:
            # raise an exception
            raise Exception('Milliseconds is required');
        
        # return obj
        return self.obj
