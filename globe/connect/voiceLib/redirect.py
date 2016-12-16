class Redirect:
    # capture to when class is instantiated
    #
    # @param    string      to
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

    # required setter
    #
    # @param    string      required
    # @return   instance    self
    def setRequired(self, required):
        self.obj['required'] = required
        return self
    
    # object getter
    #
    # @return   object  obj
    def getObject(self):
        # loop in store objects
        for key in self.obj:
            try:
                # try if object has getObjet method
                self.obj[key] = self.obj[key].getObject()
            except:
                # do nothing
                None
        
        # check if to is not set
        if 'to' not in self.obj:
            # raise an exception
            raise Exception('To is required')
        
        # return obj
        return self.obj
