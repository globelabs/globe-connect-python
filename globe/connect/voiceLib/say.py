class Say:
    # capture value when class is instantiated
    #
    # @param    string      value
    def __init__(self, value):
        self.obj = {}
        self.obj['value'] = value
    
    # as setter
    #
    # @param    string      as
    # @return   instance    self
    def setAs(self, a):
        self.obj['as'] = a
        return self

    # event setter
    #
    # @param    string      event
    # @return   instance    self
    def setEvent(self, e):
        self.obj['event'] = e
        return self

    # required setter
    #
    # @param    string      required
    # @return   instance    self
    def setRequired(self, required):
        self.obj['required'] = required
        return self

    # voice setter
    #
    # @param    string      voice
    # @return   instance    self
    def setVoice(self, voice):
        self.obj['voice'] = voice
        return self

    # allowSignals setter
    #
    # @param    string      allow
    # @return   instance    self
    def setAllowSignals(self, allow):
        self.obj['allowSignals'] = allow
        return self

    # name setter
    #
    # @param    string      name
    # @return   instance    self
    def setName(self, name):
        self.obj['name'] = name
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
        
        # check if value is not set
        if 'value' not in self.obj:
            # raise an exception
            raise Exception('Value is required')
        
        # check if event is not set
        if 'event' not in self.obj:
            # return obj as it is
            return self.obj
        
        # init say object
        say = {}
            # loop in event
        for i in range(0, len(self.obj['event'])):
            # store event values on say object
            say[i] = self.obj['event'][i]
        
        # append value to say object
        say[len(self.obj['event'])] = { 'value' : self.obj['value'] }
        # return say object
        return say;

