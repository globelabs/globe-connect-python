# Globe Oauth API
import pycurl, json, os
from StringIO import StringIO as BytesIO

# GLOBAL SECTION
# request endpoints
SUBS_URL = "https://developer.globelabs.com.ph/dialog/oauth?app_id=%s"
TOKEN_URL = "https://developer.globelabs.com.ph/oauth/access_token?app_id=%s&app_secret=%s&code=%s"

class Oauth:
    # caption app key and app secret when class is instanciated
    #
    # @param    string      key     app key
    # @param    string      secret  app secret
    def __init__(self, key, secret):
        # set key to self
        self.key = key
        # set secret to self
        self.secret = secret
    
    # authentication url getter
    #
    # @return   string      url     authentication url
    def getRedirectUrl(self):
        # return authentication url
        return (SUBS_URL % (self.key))
    
    # access token getter
    #
    # @param    string      code    authetication code
    # @return   string      token   access token
    def getAccessToken(self, code):
        # prepare request url
        url = (TOKEN_URL % (self.key, self.secret, code))

        # prepare certificate file information
        certFile = BytesIO()
        # get current directory
        certFile.write(os.getcwd())
        # append certificate path
        certFile.write("/globe/globe.crt")
        # prepare certificate
        certFile = certFile.getvalue()
        
        # instanciate response
        response = BytesIO()
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # set request to post
        c.setopt(pycurl.POST, 1)
        # ssl verification to true
        c.setopt(pycurl.SSL_VERIFYPEER, 1)
        c.setopt(pycurl.SSL_VERIFYHOST, 2)
        # set certifcate path
        c.setopt(pycurl.CAINFO, certFile)
        # write response
        c.setopt(c.WRITEDATA, response)
        # perform curl
        c.perform()

        # return curl response
        return response.getvalue()
