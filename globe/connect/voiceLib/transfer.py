class Transfer:
    # capture to when class is instantiated
    #
    # @param    string      to
    def __init__(self, to):
        self.obj = {}
        self.obj['to'] = to
    
    # answerOnMedia setter
    #
    # @param    string      ans
    # @return   instance    self
    def setAnswerOnMedia(self, ans):
        self.obj['setAnswerOnMedia'] = ans
        return self

    # choices setter
    #
    # @param    instance    choices
    # @return   instance    self
    def setChoices(self, choices):
        self.obj['choices'] = choices
        return self

    # from setter
    #
    # @param    string      fr
    # @return   instance    self
    def setFrom(self, fr):
        self.obj['from'] = fr
        return self

    # headers setter
    #
    # @param    string      headers
    # @return   instance    self
    def setHeaders(self, headers):
        self.obj['headers'] = headers
        return self

    # on setter
    #
    # @param    instance    on
    # @return   instance    self
    def setOn(self, on):
        self.obj['on'] = on
        return self

    # required setter
    #
    # @param    string      required
    # @return   instance    self
    def setRequired(self, required):
        self.obj['required'] = required
        return self

    # terminator setter
    #
    # @param    string      terminator
    # @return   instance    self
    def setTerminator(self, terminator):
        self.obj['terminator'] = terminator
        return self

    # timeout setter
    #
    # @param    string      timeout
    # @return   instance    self
    def setTimeout(self, timeout):
        self.obj['timeout'] = timeout
        return self

    # allowSignals setter
    #
    # @param    string      allow
    # @return   instance    self
    def setAllowSignals(self, allow):
        self.obj['allowSignals'] = allow
        return self

    # interDigiitTimeout setter
    #
    # @param    string      idTimeout
    # @return   instance    self
    def setInterdigitTimeout(self, idtimeout):
        self.obj['interdigitTimeout'] = idtimeout
        return self

    # ringRepeat setter
    #
    # @param    string      ringrepeat
    # @return   instance    self
    def ringRepeat(self, ringrepeat):
        self.obj['ringRepeat'] = ringrepeat
        return self

    # machineDetection setter
    #
    # @param    string      mdetection
    # @return   instance    self
    def setMachineDetection(self, mdetection):
        self.obj['machineDetection'] = mdetection
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

        # check if to is not set
        if 'to' not in self.obj:
            # raise an exception
            raise Exception('To is required')
        
        # check if name is not set
        if 'name' not in self.obj:
            # raise an exception
            raise Exception('Name is required')

        # check if choices is not set
        if 'choices' not in self.obj:
            # raise an exception
            raise Exception('Choices is required')
        
        # check if headers is not set
        if 'headers' not in self.obj:
            # raise an exception
            raise Exception('Headers is required')
        
        # return obj
        return self.obj
