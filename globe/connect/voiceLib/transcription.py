class Transcription:
    # capture id when class is instantiated
    #
    # @param    string  id
    def __init__(self, uid):
        self.obj = {}
        self.obj['id'] = uid
    
    
    # url setter
    #
    # @param    string      url
    # @return   instance    self
    def setUrl(self, url):
        self.obj['url'] = url
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
        
        # check if milliseconds is not set
        if 'id' not in self.obj:
            # raise an exception
            raise Exception('ID is required');
        
        # return obj
        return self.obj
