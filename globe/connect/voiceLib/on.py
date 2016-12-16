class On:
    # capture event and say when class is instantiated
    #
    # @param    string      event
    # @param    instance    say
    def __init__(self, event):
        self.obj = {}
        self.obj['event'] = event
    
    def setSay(self, say):
        self.obj['say'] = say
        return self

    # name setter
    #
    # @param    string      name
    # @return   instance    self
    def setName(self, name):
        self.obj['name'] = name
        return self

    # next setter
    #
    # @param    string      ext
    # @return   instance    self
    def setNext(self, next):
        self.obj['next'] = next
        return self

    # required setter
    #
    # @param    string      required
    # @return   instance    self
    def setRequired(self, required):
        self.obj['required'] = required

    # ask setter
    #
    # @param    instance    ask
    # @return   instance    self
    def setAsk(self, ask):
        self.obj['ask'] = ask
        return self

    # message setter
    #
    # @param    instance    message
    # @return   instance    self
    def setMessage(self, message):
        self.obj['message'] = message
        return self

    # wait setter
    #
    # @param    instance    wait
    # @return   instance    self
    def setWait(self, wait):
        self.obj['wait'] = wait
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
        
        # check if event is not set
        if 'event' not in self.obj:
            # raise an exception
            raise Exception('Event is required')
        
        # check if say is not set
        if 'say' not in self.obj:
            # raise an exception
            raise Exception('Say is required')
        
        # return obj
        return self.obj
