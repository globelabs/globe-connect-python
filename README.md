# Globe Connect for Python

## Introduction
Globe Connect for Python provides an implementation of Globe APIs e.g Authentication, Amax,
Sms etc. that is easy to use and can be integrated in your existing Python application. Below shows
some samples on how to use the API depending on the functionality that you need to integrate in your
application.

## Basic Usage

###### Figure 1. Authentication


```python
from globe.connect import oauth
oauth = oauth.Oauth("[key]", "[secret]")

# get redirect url
print oauth.getRedirectUrl()

# get access token
print oauth.getAccessToken("[code]")
```

###### Figure 2. Amax


```python
from globe.connect import amax
amax = amax.Amax("[app_id]", "[app_secret]")
amax.sendReward("[address]", "[token]", "[promo]")
print amax.getResponse()
```
or
```python
from globe.connect import amax
amax = amax.Amax("[app_id]", "[app_secret]")
amax.setAddress("[address]")
amax.setToken("[token]")
amax.setPromo("[promo]")
amax.sendReward()
print amax.getResponse()
```

###### Figure 3. Binary SMS

```python
from globe.connect import sms
sms = sms.Sms("[shortcode]","[token]")
print sms.sendBinary("[address]", "[msg]", "[header]", "[encoding]")
```
or
```python
from globe.connect import sms
sms = sms.setUserDataHeader("[header]")
sms.setDataEncodingScheme("[encoding]")
sms.setReceiverAddress("[address]")
sms.setMessage("[msg]")
sms.sendBinaryMessage()
print sms.getResponse()
```

###### Figure 4. Location

```python
from globe.connect import location
loc = location.Location("[token]")
loc.getLocation("[address]", "[accuracy]")
print loc.getResponse()
```
or
```python
from globe.connect import location
loc = location.Location("[token]")
loc.setAddress("[address]")
loc.setRequestedAccuracy("[accuracy]")
loc.getLocation()
print loc.getResponse()
```

###### Figure 5. Payment (Send Payment Request)

```python
from globe.connect import payment
payment = payment.Payment("[token]")
payment.sendPaymentRequest("[number]", "[amount]", "[description]", "[referenceCode]", "[status]")
print payment.getResponse()
```
or

```python
from globe.connect import payment
payment = payment.Payment("[token]")
payment.setAmount("[amount]")
payment.setDescription("[description]")
payment.setEndUserId("[number]")
payment.setReferenceCode("[referenceCode]")
payment.setTransactionOperationStatus("[status]")
payment.sendPaymentRequest()
print payment.getResponse()
```

###### Figure 6. Payment (Get Last Reference ID)

```python
from globe.connect import payment
payment = payment.Payment("[token]")
payment.getLastReferenceCode("[app_key]",  "[app_secret]")
print payment.getResponse()
```
or
```python
from globe.connect import payment
payment = payment.Payment("[token]")
payment.setAppKey("[app_key]")
payment.setAppSecret("[app_secret]")
payment.getLastReferenceCode()
print payment.getResponse()
```

###### Figure 7. Sms


```python
from globe.connect import sms
sms = sms.Sms("[shortcode]","[token]")
sms.sendMessage("[receiver_address]", "[message]", "[correlator]")
print sms.getResponse()
```
or

```python
from globe.connect import sms
sms = sms.Sms("[shortcode]","[token]")
sms.setReceiverAddress("[receiver_address]")
sms.setMessage("[message]")
sms.setClientCorrelator("[correlator]")
print sms.getResponse()
```


###### Figure 8. Subscriber (Get Balance)


```python
from globe.connect import subscriber
subscriber = subscriber.Subscriber("[token]")
subscriber.getSubscriberBalance("[address]")
print subscriber.getResponse()
```
or
```python
from globe.connect import subscriber
subscriber = subscriber.Subscriber("[token]")
subscriber.setAddress("[address]")
subscriber.getSubscriberBalance()
print subscriber.getResponse()
```

###### Figure 9. Subscriber (Get Reload Amount)



```python
from globe.connect import subscriber
subscriber = subscriber.Subscriber("[token]")
subscriber.getReloadAmount("[address]")
print subscriber.getResponse()
```
or
```python
from globe.connect import subscriber
subscriber = subscriber.Subscriber("[token]")
subscriber.setAddress("[address]")
subscriber.getReloadAmount()
print subscriber.getResponse()
```

###### Figure 10. USSD (Send)


```python
from globe.connect import ussd
ussd = ussd.Ussd("[token]", "[shortcode]")
ussd.sendUsssdRequest("[address]", "[messsage]", "[flash]")
print ussd.getResponse()
```
or
```python
from globe.connect import ussd
ussd = ussd.Ussd("[token]", "[shortcode]")
ussd.setAddress("[address]")
ussd.setMessage("[message]")
ussd.setFlash("[flash]")
ussd.sendUsssdRequest()
print ussd.getResponse()
```

###### Figure 11. USSD (Reply)


```python
from globe.connect import ussd
ussd = ussd.Ussd("[token]", "[shortcode]")
ussd.replyUssdRequest("[address]", "[message]", "[flash]", "[session_id]")
print ussd.getResponse()
```
or
```python

from globe.connect import ussd
ussd = ussd.Ussd("[token]", "[shortcode]")
ussd.setAddress("[address]")
ussd.setMessage("[message]")
ussd.setFlash("[flash]")
ussd.setSessionId("[session_id]")
ussd.replyUssdRequest()
print ussd.getResponse()
```
