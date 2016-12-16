import json

class Ask:
    # capture say when class is instanciated
    def __init__(self, say):
        self.obj = {}
        self.obj['say'] = say
    
    # choices setter
    #
    # @param    instance    choices
    # @return   instance    self
    def setChoices(self, choices):
        self.obj['choices'] = choices
        return self

    # max attemt setter
    #
    # @param    string      attempt
    # @return   instance    self
    def setMaxAttempt(self, attempt):
        self.obj['maxAttempt'] = attempt
        return self

    # bargein setter
    #
    # @param    string      bargein
    # @return   instance    self
    def setBargein (self, bargein):
        self.obj['bargein'] = bargein
        return self

    # minConfidence setter
    #
    # @param    string      confidence
    # @return   instance    self
    def setMinConfidence(self, confidence):
        self.obj['minConfidence'] = confidence
        return self

    # name setter
    #
    # @param    string      name
    # @return   instance    self
    def setName(self, name):
        self.obj['name'] = name
        return self

    # recognizer setter
    #
    # @param    string      recognizer
    # @return   instance    self
    def setRecognizer(self, recognizer):
        self.obj['recognizer'] = recognizer
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
        return self;

    # interDigitTimeout setter
    #
    # @param    string      idTimeout
    # @return   instance    self
    def setInterdigitTimeout(self, idTimeout):
        self.obj['interdigitTimeout'] = idTimeout;
        return self

    # sensitivity setter
    #
    # @param    string      sensitivity
    # @return   instance    self
    def setSensitivity(self, sensitivity):
        self.obj['sensitivity'] = sensitivity
        return self

    # speechCompleteTimeout setter
    #
    # @param    string      scTimeout
    # @return   instance    self
    def setSpeechCompleteTimeout(self, scTimeout):
        self.obj['speechCompleteTimeout'] = scTimeout
        return self

    # speechIncompleteTimeout setter
    #
    # @param    string      siTimeout
    # @return   instance    self
    def setSpeechIncompleteTimeout(self, siTimeout):
        self.obj['speechIncompleteTimeout'] = siTimeout
        return self
    
    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # loop in obj
        for key in self.obj:
            try:
                # check if obj has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if choices is not set
        if 'choices' not in self.obj:
            # raise an exception
            raise Exception('Choices is required.')
        
        # check if say is not set
        if 'say' not in self.obj:
            # raise an exception
            raise Exception('Say is required')
        
        # return obj
        return self.obj;

