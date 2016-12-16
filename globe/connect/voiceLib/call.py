import json

class Call:
    # capture to when class is instanciated
    #
    # @param    string  to
    def __init__(self, to):
        self.obj = {}
        self.obj['to'] = to

    # name setter
    #
    # @param    string      name
    # @return   instance    self
    def setName(self, name):
        self.obj['name'] = name
        return self

    # answerToMedia setter
    #
    # @param    string      ansMedia
    # @return   instance    self
    def setAnswerToMedia(self, ansMedia):
        self.obj['answerToMedia'] = ansMedia
        return self

    # channel setter
    #
    # @param    string      channel
    # @return   instance    self
    def setChannel (self, channel):
        self.obj['channel'] = channel
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
        self.obj['headers'] = header
        return self

    # recording setter
    #
    # @param    instance    recording
    # @return   instance    self
    def setRecording(self, recodring):
        self.obj['recording'] = recording
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

    # allSignals setter
    #
    # @param    string      signal
    # @return   instance    self
    def setAllSignals(self, signal):
        self.obj['allowSignals'] = signal
        return self

    # machineDetection setter
    #
    # @param    instance    mDetection
    # @return   instance    self
    def setMachineDetection(self, mDetection):
        self.obj['machineDetection'] = mDetection
        return self

    # object getter
    #
    # @return   object      obj
    def getObject(self):
        # loop in stored obj
        for key in self.obj:
            try:
                # try if obj has getObject method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if to is not set
        if 'to' not in self.obj:
            # raise an exception
            raise Exception('to is required');
        
        # return obj
        return self.obj;
