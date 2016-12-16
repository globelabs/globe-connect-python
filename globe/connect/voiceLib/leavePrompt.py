class LeavePrompt:
    # capture value when class is instantiated
    #
    # @param    string      value
    def __init__(self, value):
        self.obj = {};
        self.obj['value'] = value
    
    # voice setter
    #
    # @param    string      voice
    # @return   instance    self
    def setVoice(self, voice):
        self.obj['voice'] = voice
        return self
    
    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # loop in store objects
        for key in self.obj:
            try:
                # try if object has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if value is not set
        if 'value' not in self.obj:
            # raise an exception
            raise Exception('Leave prompt value is required.')
        
        # return obj
        return self.obj
