import json

class Conference:
    # capture id when class is instantiated
    #
    # @param    string      id
    def __init__(self, id):
        self.obj = {}
        self.obj['id'] = id
    
    # mute setter
    #
    # @param    string      mute
    # @return   instance    self
    def setMute(self, mute):
        self.obj['mute'] = mute
        return self

    # name setter
    #
    # @param    string      name
    # @return   instance    self
    def setName(self, name):
        self.obj['name'] = name
        return self

    # playTones setter
    #
    # @param    string      playTones
    # @return   instance    self
    def setPlayTones(self, playTones):
        self.obj['playTones'] = playTones
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

    # allow signals setter
    #
    # @param    string      allowsignals
    # @return   instance    self
    def setAllowSignals(self, allowSignals):
        self.obj['allowSignals'] = allowSignals
        return self

    # interdigitTimeout setter
    #
    # @param    string      idTimeout
    # @return   instance    self
    def setInterDigitTimeout(self, idTimeout):
        self.obj['interDigitTimeout'] = idTimeout
        return self

    # joinPrompt setter
    #
    # @param    instance    jPrompt
    # @return   instance    self
    def setJoinPrompt(self, jPrompt):
        self.obj['joinPrompt'] = jPrompt
        return self

    # leavePrompt setter
    #
    # @param    instance    lPrompt
    # @return   instance    self
    def setLeavePrompt(self, lPrompt):
        self.obj['leavePrompt'] = lPrompt
        return self

    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # loop in stored obj
        for key in self.obj:
            try:
                # try if object has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if id is not set
        if 'id' not in self.obj:
            # raise an exception
            raise Exception('Conference id is required.')
        
        # return obj
        return self.obj
