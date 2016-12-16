# Globe Payment API

# import section
import pycurl, json
from StringIO import StringIO as BytesIO

# Global section
# charging endpoint
CHARGE_URL = "https://devapi.globelabs.com.ph/payment/v1/transactions/amount?access_token=%s"
# last reference code endpoint
REFCODE_URL = "https://devapi.globelabs.com.ph/payment/v1/transactions/getLastRefCode?app_id=%s&app_secret=%s"


class Payment:
    # capture token when class is instanciated
    # @param string token
    def __init__(self, token):
        # set token
        self.token = token

        # set variables to None by default
        self.to = None
        self.amount = None
        self.desc = None
        self.refCode = None
        self.status = None
        self.key = None
        self.secret = None
    
    # amount setter
    #
    # @param    string      amount  charging amount
    # @return   instance    self
    def setAmount(self, amount):
        self.amount = amount
        return self
    
    # description setter
    #
    # @param    string      desc    charging description
    # @return   instance    self
    def setDescription(self, desc):
        self.desc = desc
        return self

    # user id setter
    #
    # @param    string      user    number
    # @return   instance    self
    def setEndUserId(self, to):
        self.to = to
        return self

    # reference code setter
    #
    # @param    string      refCode reference code
    # @return   instance    self
    def setReferenceCode(self, refCode):
        self.refCode = refCode
        return self
    
    # transactin status setter
    #
    # @param    string      status  transaction operation status
    # @return   instance    self
    def setTransactionOperationStatus(self, status):
        self.status = status
        return self
    
    # app key setter 
    #
    # @param    string      key     app key   
    # @return   instance    self
    def setAppKey(self, key):
        self.key = key
        return self

    # app secret setter 
    #
    # @param    string      secret  app secret
    # @return   instance    self
    def setAppSecret(self, secret):
        self.secret = secret
        return self

    # get last reference code
    #
    # @param    string      key(optional)       app key
    # @param    string      secret(optional)    app secret
    # @return   instance    self
    def getLastReferenceCode(self, key = None, secret = None):
        # if key is set
        if key is not None:
            # set key to self
            self.key = key

        # if secret is set
        if secret is not None:
            # set secret to self
            self.secret = secret
        
        # prepare request url
        url = (REFCODE_URL % (self.key, self.secret))
        
        # instanciate response
        response = BytesIO()

        # instanciate curl
        c = pycurl.Curl()
        # set url
        c.setopt(c.URL, url)
        # write response
        c.setopt(c.WRITEDATA, response)
        # perform request
        c.perform()

        # store response to self
        self.responseBody = response.getvalue()
        # return self
        return self

    # charge subscriber
    #
    # @param    string      to (optional)       end user id(user number)
    # @param    string      amount (optional)   charging amount in string
    # @param    string      desc (optional)     charging description
    # @param    string      refCode (optional)  charging reference code
    # @param    string      status (optional)   charging status
    def sendPaymentRequest(self, to = None, amount = None, desc = None, refCode = None, status = None):
        # prepare request url
        url = (CHARGE_URL % (self.token))
        
        # if to is set
        if to is not None:
            # set to to self
            self.to = to
        
        # if amount is set
        if amount is not None:
            # set amount to self
            self.amount = amount
        
        # if desc is set
        if desc is not None:
            # set desc to self
            self.desc = desc
        
        # if reCode is set
        if refCode is not None:
            # set refCode to self
            self.refCode = refCode

        # if status is set
        if status is not None:
            # set status to self
            self.status = status

        # prepare request payload
        payload = BytesIO()
        
        # compose amount payload
        payload.write("amount=")
        payload.write(self.amount)
        payload.write("&")
        
        # compose description payload
        payload.write("description=")
        payload.write(self.desc)
        payload.write("&")

        # compose endUserId payload
        payload.write("endUserId=")
        payload.write(self.to)
        payload.write("&")

        # compose referenceCode payload
        payload.write("referenceCode=")
        payload.write(self.refCode)
        payload.write("&")

        # compose transactionOperationStatus payload
        payload.write("transactionOperationStatus=")
        payload.write(self.status)

        # get composed payload
        payload = payload.getvalue()

        # instanciate response
        response = BytesIO()
        
        # instanciate curl
        c = pycurl.Curl()
        # set request url
        c.setopt(c.URL, url)
        # set request to post
        c.setopt(pycurl.POST, 1)
        # provide post payload
        c.setopt(pycurl.POSTFIELDS, payload)
        # write response to response
        c.setopt(c.WRITEDATA, response)
        # perform request
        c.perform()

        # store response to sefl
        self.responseBody = response.getvalue()
        # return self
        return self
    
    # response getter
    #
    # @return   string      responseBody    response data
    def getResponse(self):
        return self.responseBody
