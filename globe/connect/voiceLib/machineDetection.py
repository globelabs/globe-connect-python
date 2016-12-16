class MachineDetection:
    def __init__(self):
        self.obj = {}
    
    # introduction setter
    #
    # @param    string      introduction
    # @return   instance    self
    def setIntroduction(self, introduction):
        self.obj['introduction'] = introduction
        return self

    # voice setter
    #
    # @param    string      voice
    # @return   instance    self
    def setVoice(self, voice):
        self.obj['voice'] = voice
        return self

    # object getter
    #
    # @return   object      obj
    def getObject(self):
        # loop in stored objects
        for key in self.obj:
            try:
                # try if object has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # return obj
        return self.obj
