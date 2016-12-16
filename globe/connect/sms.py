# Globe SMS API

# import section
import pycurl, json
from StringIO import StringIO as BytesIO

# Global Section

# request endpoints
# send endpoint
SEND_URL = "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/%s/requests?access_token=%s"
# send binary endpoint
BINARY_URL = "https://devapi.globelabs.com.ph/binarymessaging/v1/outbound/%s/requests?access_token=%s"

class Sms:
    # capture sender and token when class is instanciated
    #
    # @param    string      sender  app short code
    # @param    string      token   authenticated token
    def __init__(self, sender, token):
        # set token to self
        self.token = token
        # set sender to self
        self.sender = sender

        # set variables to None as default
        self.correlator = None
        self.address = None
        self.msg = None
        self.header = None
        self.encoding = None
    
    # client correlator setter
    #
    # @param    string      correlator  cleint correlator
    # @return   instance    self
    def setClientCorrelator(self, correlator):
        self.correlator = correlator
        return self
    
    # reciever address setter
    #
    # @param    string      address     receiver address
    # @return   instance    self
    def setReceiverAddress(self, address):
        self.to = address
        return self
    
    # message setter
    #
    # @param    string      msg     message
    # @return   instance    self
    def setMessage(self, msg):
        self.msg = msg
        return self

    # user data header setter
    #
    # @param    string      header  user data header
    # @return   instance    self
    def setUserDataHeader(self, header):
        self.header = header
        return self
    
    # data encoding scheme setter
    #
    # @param    string  encoding    data encoding scheme
    # @return   instance self
    def setDataEncodingScheme(self, encoding):
        self.encoding = encoding
        return self
    
    # send message
    #
    # @param    string      to(optional)            receiver address
    # @param    string      msg(optional)           message
    # @param    string      correlator(optional)    client correlator
    # @return   instance    self
    def sendMessage(self, to=None, msg=None, correlator=None):
        # if to is set
        if to is not None:
            # set to to self
            self.to = to
        
        # if msg is set
        if msg is not None:
            # set msg to self
            self.msg = msg
        
        # if correlator is set
        if correlator is not None:
            # set correlator to self
            self.correlator = correlator
        
        # proper format for numbers
        sformat = "tel:%s"
        # set to to proper format
        self.to = (sformat % (self.to))
        # prepare request url
        url = (SEND_URL % (self.sender, self.token))
        # set sender to proper format
        sender = (sformat % (self.sender))
        # instanciate response
        response = BytesIO()

        # prepare request payload as list
        payload = {
            "outboundSMSMessageRequest": {
                "senderAddress": sender,
                "outboundSMSTextMessage": {
                    "message" : self.msg},
                "address" : [self.to]}}
        
        # if correlator is set
        if self.correlator is not None:
            # add correlator to request payload
            payload['outboundSMSMessageRequest']['clientCorrelator'] = self.correlator
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # set JSON header
        c.setopt(pycurl.HTTPHEADER, ['Content-type: application/json'])
        # set request to post
        c.setopt(pycurl.POST, 1)
        # set json payload
        c.setopt(pycurl.POSTFIELDS, json.dumps(payload))
        # write response to response
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()

        # set response to self
        self.responseBody = response.getvalue()
        # return self
        return self
    
    # send binary message
    #
    # @param    string      to(optional)        receiver address
    # @param    string      msg(optional)       message
    # @param    string      header(optiona)     user data header
    # @param    string      encoding(optional)  data encoding scheme
    def sendBinaryMessage(self, to = None, msg = None, header = None, encoding = None):
        # prepare request url
        url = (BINARY_URL % (self.sender, self.token))
        
        # if to is set
        if to is not None:
            # set to to self
            self.to = to
        
        # if msg is set
        if msg is not None:
            # set msg to self
            self.msg = msg
        
        # if header is set
        if header is not None:
            # set header to self
            self.header = header
        
        # if encoding is set
        if encoding is not None:
            # set encoding to self
            self.encoding = encoding
        
        # prepare request payload as list
        payload = {"outboundBinaryMessageRequest" : {
            "userDataHeader"            : self.header,
            "dataCodingScheme"          : self.encoding,
            "address"                   : self.to,
            "outboundBinaryMessage"     : {
                "message" : self.msg
            },

            "senderAddress"             : self.sender,
            "access_token"              : self.token}}
        
        # instanciate response
        response = BytesIO()
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # set JSON header
        c.setopt(pycurl.HTTPHEADER, ['Content-type: application/json'])
        # set request to post
        c.setopt(pycurl.POST, 1)
        # set json payload
        c.setopt(pycurl.POSTFIELDS, json.dumps(payload))
        # write response to response
        c.setopt(pycurl.WRITEDATA, response)
        # perform curl
        c.perform()
        
        # set response to self
        self.responseBody = response.getvalue()
        # return self
        return self
    
    # response getter
    #
    # @return   instance    self
    def getResponse(self):
        # return stored response
        return self.responseBody



