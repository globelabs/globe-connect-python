class StartRecording:
    # capture url when class is instantiated
    #
    # @param    string      url
    def __init__(self, url):
        self.obj = {}
        self.obj['url'] = url
    
    # format setter
    #
    # @param    string      frmat
    # @return   instance    self
    def setFormat(self, frmat):
        self.obj['format'] = frmat
        return self

    # method setter
    #
    # @param    string      method
    # @return   instance    self
    def setMethod(self, method):
        self.obj['method'] = method
        return self

    # username setter
    #
    # @param    string      username
    # @return   instance    self
    def setUsername(self, username):
        self.obj['username'] = username
        return self

    # password setter
    #
    # @param    string      password
    # @return   instance    self
    def setPassword(self, password):
        self.obj['password'] = password
        return self

    # transcriptionId setter
    #
    # @param    string      transId
    # @return   instance    self
    def setTranscriptionId(self, transId):
        self.obj['transcriptionID'] = transId
        return self

    # transcriptionEmailFormat setter
    #
    # @param    string      transFormat
    # @return   instance    self
    def setTranscriptionEmailFormat(self, transFormat):
        self.obj['transriptionEmailFormat'] = transFormat
        return self

    # transcriptionOutUri setter
    #
    # @param    string      transUri
    # @return   instance    self
    def setTranscriptionOutUri(self, transUri):
        self.obj['transcriptionOutURI'] = transUri;
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
        
        # check if url is not set
        if 'url' not in self.obj:
            # raise an exception
            raise Exception('Url is required')
        
        # return obj
        return self.obj
