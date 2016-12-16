class JoinPrompt:
    # capture value when class is instantiated
    #
    # @param    string      value
    def __init__(self, value):
        self.obj = {}
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
        # loop in stored object
        for key in self.obj:
            try:
                # try if object has getMethod method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check value if not set
        if 'value' not in self.obj:
            # raise an exception
            raise Exception('Join Prompt is required')
        
        # return obj
        return self.obj
