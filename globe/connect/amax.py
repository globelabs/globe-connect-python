# Globe Amax API

# import section
import pycurl, json
from StringIO import StringIO as BytesIO

# Global section
# request enpoints
REWARD_URL = "https://devapi.globelabs.com.ph/rewards/v1/transactions/send"

class Amax:
    # capture app id and app secret when class is instanciated
    #
    # @param    string      key     app id
    # @param    string      secert  app secret
    def __init__(self, key, secret):
        # set key to self
        self.key = key
        # set secret to self
        self.secret = secret

        # set variables value to None as default
        self.address = None
        self.token = None
        self.promo = None
    
    # address setter
    #
    # @param    string      address     customer number
    # @return   instance    self
    def setAddress(self, address):
        self.address = address
        return self
    
    # token setter
    #
    # @param    string      token   access token
    # @return   instance    self
    def setToken(self, token):
        self.token = token
        return self

    # promo setter
    #
    # @param    string      promo   defined promo
    # @return   instance    self
    def setPromo(self, promo):
        self.promo = promo
        return self

    # sender reward
    #
    # @param    string      address (optional)      customer number
    # @param    string      token (optional)        access token
    # @param    string      promo (optional)        defined promo
    # @return   instance    self
    def sendReward(self, address = None, token = None, promo = None):
        # prepare reward
        url = REWARD_URL
        
        # if address is set
        if address is not None:
            # set address to self
            self.address = address
        
        # if token is set
        if token is not None:
            # set token to self
            self.token = token
        
        # if promo is set
        if promo is not None:
            # set promo to self
            self.promo = promo

        # prepare request payload
        payload = {
            "outboundRewardRequest" : {
                "app_id" : self.key,
                "app_secret" : self.secret,
                "rewards_token" : self.token,
                "address" : self.address,
                "promo" : self.promo } }
        
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
        # set json post payload
        c.setopt(c.POSTFIELDS, json.dumps(payload))
        # write response to response
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()
        
        # store response to self
        self.responseBody = response.getvalue()
        # return self
        return self
    
    # response getter
    #
    # @return   string  responseBody    stored response
    def getResponse(self):
        return self.responseBody
