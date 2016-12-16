class Message:
    # capture say and to when class is instantiated
    #
    # @param    instance    say
    # @param    string      to
    def __init__(self, say, to):
        self.obj = {}
        self.obj['say'] = say
        self.obj['to'] = to
    
    # name setter
    #
    # @param    string      name
    # @return   instance    self
    def setName(self, name):
        self.obj['name'] = name
        return self

    # answerOnMedia setter
    #
    # @param    string      ansMedia
    # @return   instance    self
    def setAnswerOnMedia(self, ansMedia):
        self.obj['answerOnMedia'] = ansMedia
        return self

    # channel setter
    #
    # @param    string      channel
    # @return   instance    self
    def setChannel(self, channel):
        self.obj['channel'] = channel
        return self

    # from setter
    #
    # @param    string      fr
    # @return   instance    self
    def setFrom(self, fr):
        self.obj['from'] = fr
        return self

    # network setter
    #
    # @param    string      network
    # @return   instance    self
    def setNetwork(self, network):
        self.obj['network'] = network
        return self

    # required setter
    #
    # @param    string      required
    # @return   instance    self
    def setRequired(self, required):
        self.obj['required'] = required
        return self

    # timeout setter
    #
    # @param    string      timeout
    # @return   instance    self
    def setTimeout(self, timeout):
        self.obj['timeout'] = timeout
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
        
        # check if say is not set
        if 'say' not in self.obj:
            # raise an exception
            raise Exception('Say is required')
        
        # check if to is not set
        if 'to' not in self.obj:
            # raise an exception
            raise Exception('To is required')
        
        # return obj
        return self.obj
