# Globe Subscriber API
# import section
import pycurl, json
from StringIO import StringIO as BytesIO

# Global section
# subscriber balance endpoint
BALANCE_URL = "https://devapi.globelabs.com.ph/location/v1/queries/balance?access_token=%s&address=%s"
RELOAD_URL = "https://devapi.globelabs.com.ph/location/v1/queries/reload_amount?access_token=%s&address=%s"

class Subscriber:
    # capture token when class is instanciated
    #
    # @params   string  token
    def __init__(self, token):
        self.token = token
        self.address = None


    # setAddress address setter
    #
    # @param    string    address    subscriber address
    # @return   instance  self 
    def setAddress(self, address):
        # set address to self instance
        self.address = address
        # return self
        return self

    # get subscriber balance
    #
    # @param    string      address (optional)   subscriber address
    # @return   instance    self
    def getReloadAmount(self, address = None):
        if address is not None:
            self.address = address

        url = (RELOAD_URL % (self.token, self.address))
        # instanciate response string
        response = BytesIO()
        
        # instanciate pycurl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # write response to responce instance
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()

        # store curl response to self instance 
        self.responseBody = response.getvalue()
        # return self
        return self

    
    # get subscriber balance
    #
    # @param    string      address (optional)   subscriber address
    # @return   instance    self
    def getSubscriberBalance(self, address = None):
        # if parameter address is set
        if address is not None:
            # set address to self instance
            self.address = address
        
        # perapare request url
        url = (BALANCE_URL % (self.token, self.address))
        # instanciate response string
        response = BytesIO()
        
        # instanciate pycurl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # write response to responce instance
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()

        # store curl response to self instance 
        self.responseBody = response.getvalue()
        # return self
        return self
    # return curl response that is stored earlier
    #
    # @return   string response
    def getResponse(self):
        # return response
        return self.responseBody
