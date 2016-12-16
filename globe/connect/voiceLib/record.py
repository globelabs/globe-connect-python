class Record:
    # capture name and url when class is instantiated
    #
    # @param    string      name
    # @param    string      url
    def __init__(self, name, url):
        self.obj = {}

        self.obj['name'] = name
        self.obj['url'] = url
    
    # attempts setter
    #
    # @param    string      attempts
    # @return   instance    self
    def setAttempts(self, attempts):
        self.obj['attempts'] = attempts
        return self

    # bargein setter
    #
    # @param    string      bargein
    # @return   instance    self
    def setBargein(self, bargein):
        self.obj['bargein'] = bargein
        return self

    # beep setter
    #
    # @param    string      beep
    # @return   instance    self
    def setBeep(self, beep):
        self.obj['beep'] = beep
        return self

    # choices setter
    #
    # @param    instance    choices
    # @return   instance    self
    def setChoices(self, choices):
        self.obj['choices'] = choices
        return self

    # format setter
    #
    # @param    string      format
    # @return   instance    self
    def setFormat(self, format):
        self.obj['format'] = format
        return self

    # maxSilence setter
    #
    # @param    string      silence
    # @return   instance    self
    def setMaxSilence(self, silence):
        self.obj['maxSilence'] = silence
        return self

    # maxTime setter
    #
    # @param    string      maxTime
    # @return   instance    self
    def setMaxTime(self, maxTime):
        self.obj['maxTime'] = maxTime
        return self

    # method setter
    #
    # @param    string      method
    # @return   instance    self
    def setMethod(self, method):
        self.obj['method'] = method
        return self

    # minConfedence setter
    #
    # @param    string      minConfedence
    # @return   instance    self
    def setMinConfidence(self, minConfidence):
        self.obj['minConfidence'] = minConfidence
        return self

    # required setter
    #
    # @param    string      required
    # @return   instance    self
    def setRequired(self, required):
        self.obj['required'] = required
        return self

    # say setter
    #
    # @param    instance    say
    # @return   instance    self
    def setSay(self, say):
        self.obj['say'] = say
        return self

    # timeout setter
    #
    # @param    string      timeout
    # @return   instance    self
    def setTimeout(self, timeout):
        self.obj['timeout'] = timeout
        return self

    # transcription setter
    #
    # @param    string      transcription
    # @return   instance    self
    def setTranscription(self, transcription):
        self.obj['transcription'] = transcription
        return self

    # password setter
    #
    # @param    string      password
    # @return   instance    self
    def setPassword(self, password):
        self.obj['password'] = password
        return self

    # username setter
    #
    # @param    string      username
    # @return   instance    self
    def setUsername(self, username):
        self.obj['username'] = username
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
    # @param    string      allowSignals
    # @return   instance    self
    def setAllowSignals(self, allowSignals):
        self.obj['allowSignals'] = allowSignals
        return self

    # interDigitTImeout setter
    #
    # @param    string      idTimeout
    # @return   instance    self
    def setInterdigitTimeout(self, idTimeout):
        self.obj['interDigitTimeout'] = idTimeout
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

        # check if name is not set
        if 'name' not in self.obj:
            # raise an exception
            raise Exception('Name is required')

        # check if url is not set
        if 'url' not in self.obj:
            # raise an exception
            raise Exception('Url is required')

        # return obj
        return self.obj
