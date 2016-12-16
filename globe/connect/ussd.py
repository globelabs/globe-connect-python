# Globe USSD API

# import section
import pycurl, json
from StringIO import StringIO as BytesIO

# Global Section

# request endpoints
SEND_USSD = "https://devapi.globelabs.com.ph/ussd/v1/outbound/%s/send/requests?access_token=%s"
REPLY_USSD = "https://devapi.globelabs.com.ph/ussd/v1/outbound/%s/reply/requests?access_token=%s"

class Ussd:
    # capture token and shorcode when class is instantiated
    #
    # @param    string      token       access token
    # @param    string      shortcode   app shortcode
    def __init__(self, token, shortcode):
        # set token to self
        self.token = token
        # set shortcode to self
        self.shortcode = shortcode
        
        # set variable default values
        self.address = None
        self.flash = False
        self.msg = None
        self.session = None

    # address setter
    #
    # @param    string      address     customer number
    # @return   instance    self
    def setAddress(self, address):
        self.address = address
        return self

    # flash setter
    #
    # @param    bool        flash       flash True or False
    # @return   instance    self
    def setFlash(self, flash):
        self.flash = flash
        return self

    # message setter
    #
    # @param    string      msg         ussd message
    # @return   instance    self
    def setUssdMessage(self, msg):
        self.msg = msg
        return self
    
    # session id setter
    #
    # @param    string      session     ussd session id
    # @return   instance    self
    def setSessionId(self, session):
        self.session = session
        return self
    
    # send ussd request
    #
    # @param    string      address (optional)  customer address
    # @param    string      msg (optional)      ussd message
    # @param    bool        flash (optional)    flash True or False
    # @return   instance    self
    def sendUssdRequest(self, address = None, msg = None, flash = None):
        # prepare request url
        url = (SEND_USSD % (self.shortcode, self.token))
        
        # if address is set
        if address is not None:
            # set address to self
            self.address = address

        # if msg is set
        if msg is not None:
            # set msg to self
            self.msg = None

        # if flash is set
        if flash is not None:
            # set flash to self
            self.flash = flash
        
        # prepare request payload
        payload = {
            "outboundUSSDMessageRequest" : {
                "outboundUSSDMessage" : {
                    "message" : self.msg
                },
                "address" : self.address,
                "senderAddress" : self.shortcode,
                "flash" : self.flash }}
        
        # instanciate response string
        response = BytesIO()
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # set json header
        c.setopt(c.HTTPHEADER, ["Content-type: application/json"])
        # set request to post
        c.setopt(c.POST, True)
        # set json payload
        c.setopt(c.POSTFIELDS, json.dumps(payload))
        # write response to response
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()
        
        # store response to self
        self.responseBody = response
        # return self
        return self

    # reply ussd request
    #
    # @param    string      address (optional)     customer number
    # @param    string      msg (optional)         ussd message
    # @param    bool        flash (optional)       flash True or False
    # @param    string      session (optional)     ussd session id
    # @return   instance    self
    def replyUssdRequest(self, address = None, msg = None, flash = None, session = None):
        # prepare request url
        url = (REPLY_USSD % (self.shortcode, self.token))
        
        # if session is set
        if session is not None:
            # set session to self
            self.session = session
        
        # if msg is set
        if msg is not None:
            # set msg to self
            self.msg = msg
        
        # if flash is set
        if flash is not None:
            # set flash to self
            self.flash = flash
        
        # if address is set
        if address is not None:
            # set address to self
            self.address = address
        
        # prepare request payload
        payload = {
            "outboundUSSDMessageRequest" : {
                "outboundUSSDMessage" : {
                    "message" : self.msg},
                "address" : self.address,
                "senderAddress" : self.shortcode,
                "sessionID" : self.session,
                "flash" : self.flash}}
        
        # instanciate response string
        response = BytesIO()
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # set json request header
        c.setopt(c.HTTPHEADER, ["Content-type: application/json"])
        # set request to post
        c.setopt(c.POST, True)
        # set post payload
        c.setopt(c.POSTFIELDS, json.dumps(payload))
        # write response to response
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()
        
        # store response to responseBody
        self.responseBody = response
        # return self
        return self

    # response getter
    #
    # @return   string  responseBody
    def getResponse(self):
        # return stored response
        return self.responseBody
