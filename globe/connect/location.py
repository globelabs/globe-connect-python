# Globe Location API

# import section
import pycurl, json
from StringIO import StringIO as BytesIO

# Global section
# request endpoints
LOCATION_URL = "https://devapi.globelabs.com.ph/location/v1/queries/location?access_token=%s&address=%s&requestedAccuracy=%s"

class Location:
    # capture token when class is instanciated
    #
    # @param    string  token   access token
    def __init__(self, token):
        # set token to self
        self.token = token

        # set variables to None as default
        self.address = None
        self.accuracy = None
    
    # address setter
    #
    # @param    string      address     user address (number)
    # @return   instance    self
    def setAddress(self, address):
        self.address = address
        return self

    # accuracy setter
    #
    # @param    string|int  accuracy    requested location accuracy
    # @return   instance    self        
    def setRequestedAccuracy(self, accuracy):
        # set accuracy to self
        self.accuracy
        return self

    # request location
    #
    # @param    string (optional)       num     user address (number)
    # @param    string|int (optional)   acc     requested location accuracy
    # @return   instance                self
    def getLocation(self, num = None, acc=None):
        # if num is set
        if num is not None:
            # set num to self.address
            self.address = num
        
        # if acc is set
        if acc is not None:
            # set acc to self.accuracy
            self.accuracy = acc
        
        # if accuracy is None
        if self.accuracy is None:
            # set accuracy to 10
            self.accuracy = 10
        
        # prepare request url
        url = (LOCATION_URL % (self.token, self.address, self.accuracy))
        
        # instanciate response
        response = BytesIO()
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # write response to response
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()

        # set response to self
        self.responseBody = response.getvalue()
        # return self
        return self
    
    # response getter
    #
    # @return   string  responseBody    stored response
    def getResponse(self):
        # return stored response
        return self.responseBody
