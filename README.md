
## Globe Connect for Python

### Setting Up

```pip install globe```

### Authentication

#### Overview

If you haven't signed up yet, please follow the instructions found in [Getting Started](http://www.globelabs.com.ph/docs/#getting-started-create-an-app) to obtain an `App ID` and `App Secret` these tokens will be used to validate most of your interaction requests with the Globe APIs.

    The authenication process follows the protocols of **OAuth 2.0**. The example code below shows how you can swap your app tokens for an access token.

#### Sample Code

```python
from globe.connect import oauth

oauth = oauth.Oauth("[key]", "[secret]")

# get redirect url
print oauth.getRedirectUrl()

# get access token
print oauth.getAccessToken("[code]")
```

#### Sample Results

```json
{
    "access_token":"1ixLbltjWkzwqLMXT-8UF-UQeKRma0hOOWFA6o91oXw",
    "subscriber_number":"9171234567"
}
```

### SMS

#### Overview

Short Message Service (SMS) enables your application or service to send and receive secure, targeted text messages and alerts to your Globe / TM subscribers.

        Note: All API calls must include the access_token as one of the Universal Resource Identifier (URI) parameters.

#### SMS Sending

Send an SMS message to one or more mobile terminals:

##### Sample Code

```python
from globe.connect import sms

sms = sms.Sms("[shortcode]","[token]")
sms.setReceiverAddress("[receiver_address]")
sms.setMessage("[message]")
sms.setClientCorrelator("[correlator]")
sms.sendMessage()

print sms.getResponse()
```

##### Sample Results

```json
{
    "outboundSMSMessageRequest": {
        "address": "tel:+639175595283",
        "deliveryInfoList": {
            "deliveryInfo": [],
            "resourceURL": "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/8011/requests?access_token=3YM8xurK_IPdhvX4OUWXQljcHTIPgQDdTESLXDIes4g"
        },
        "senderAddress": "8011",
        "outboundSMSTextMessage": {
            "message": "Hello World"
        },
        "receiptRequest": {
            "notifyURL": "http://test-sms1.herokuapp.com/callback",
            "callbackData": null,
            "senderName": null,
            "resourceURL": "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/8011/requests?access_token=3YM8xurK_IPdhvX4OUWXQljcHTIPgQDdTESLXDIes4g"
        }
    }
}
```

#### SMS Binary

Send binary data through SMS:

##### Sample Code

```python
from globe.connect import sms

sms = sms.setUserDataHeader("[header]")
sms.setDataEncodingScheme("[encoding]")
sms.setReceiverAddress("[address]")
sms.setMessage("[msg]")
sms.sendBinaryMessage()

print sms.getResponse()
```

##### Sample Results

```json
{
    "outboundBinaryMessageRequest": {
        "address": "9171234567",
        "deliveryInfoList": {
            "deliveryInfo": [],
            "resourceURL": "https://devapi.globelabs.com.ph/binarymessaging/v1/outbound/{senderAddress}/requests?access_token={access_token}",
        "senderAddress": "21581234",
        "userDataHeader": "06050423F423F4",
        "dataCodingScheme": 1,
        "outboundBinaryMessage": {
            "message": "samplebinarymessage"
        },
        "receiptRequest": {
          "notifyURL": "http://example.com/notify",
          "callbackData": null,
          "senderName": null
        },
        "resourceURL": "https://devapi.globelabs.com.ph/binarymessaging/v1/outbound/{senderAddress}/requests?access_token={access_token}"
    }
}
```

#### SMS Mobile Originating (SMS-MO)

Receiving an SMS from globe (Mobile Originating - Subscriber to Application):

##### Sample Code

```python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json

...

def _set_headers(self):
    # set response code as 200
    self.send_response(200)
    # set content-type to text/html,
    # we can also set it as application/json ;)
    self.send_header("Content-type", "text/html")
    # end header
    self.end_headers()

def do_POST(self):
    # set http header
    self._set_headers()
    # store post data
    self.data_string = self.rfile.read(int(self.headers["Content-Length"]))
    # load post data as json
    data = json.loads(self.data_string)
    # write data to response
    self.wfile.write(data)

...
```

##### Sample Results

```json
{
  "inboundSMSMessageList":{
      "inboundSMSMessage":[
         {
            "dateTime":"Fri Nov 22 2013 12:12:13 GMT+0000 (UTC)",
            "destinationAddress":"tel:21581234",
            "messageId":null,
            "message":"Hello",
            "resourceURL":null,
            "senderAddress":"9171234567"
         }
       ],
       "numberOfMessagesInThisBatch":1,
       "resourceURL":null,
       "totalNumberOfPendingMessages":null
   }
}
```

### Voice

#### Overview

The Globe APIs has a detailed list of voice features you can use with your application.

#### Voice Ask

You can take advantage of Globe's automated Ask protocols to help service your customers without manual intervention for common questions in example.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API")
choices = voice.choices("[5 DIGITS]")
askSay = voice.say("Please enter your 5 digit zip code.")

ask = voice.ask(askSay)
ask.setChoices(choices)
ask.setAttempts(3)
ask.setBargein(false)
ask.setName("foo")
ask.setRequired(true)
ask.setTimeount(10)

on = voice.on("continue")
on.setNext("http://somfakehost.com:8080/")
on.setRequired(true)

voice.addSay(askSay)
voice.addAsk(ask)
voice.addOn(on)

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API."
            }
        },
        {
            ask: {
                choices: {
                    value: "[5 DIGITS]"
                },
                attempts: 3,
                bargein: false,
                name: "foo",
                required: true,
                say: {
                    value: "Please enter your 5 digit zip code."
                },
                timeout: 10
            }
        },
        {
            on: {
                event: "continue",
                next: "http://somefakehost.com:8000/",
                required: true
            }
        }
    ]
}
```

#### Voice Answer

You can take advantage of Globe's automated Ask protocols to help service your customers without manual intervention for common questions in example.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()
say = voice.say("Welcome to my Tropo Web API")

print voice.addSay(say).getObject())
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API."
            }
        },
        {
            hangup: { }
        }
    ]
}
```

#### Voice Ask Answer

A better sample of the Ask and Answer dialog would look like the following.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API.")

if url == "/ask":
    choices = voice.choices("[5 DIGITS]")
    askSay = voice.say("Please enter your 5 digit zip code.")

    ask = voice.ask(askSay)
    ask.setChoices(choices)
    ask.setAttempts(3)
    ask.setBargein(false)
    ask.setName("foo")
    ask.setRequired(true)
    ask.setTimeout(10)

    on = voice.on("continue")
    on.setNext("/answer")
    on.setRequired(true)

    voice.addSay(say)
    voice.addAsk(ask)
    voice.addOn(on)

    obj = voice.getObject()
elif url == "/answer":
    result = voice.result(data).getObject()
    interpretation = result.actions.interpretation

    say = ("Your zip is %s, thank you!" % (interpretation))
    say = voice.say(say)
    voice.setSay(say)

    obj = voice.getObject()

print obj
```

##### Sample Results

```json
if path is ask?

{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API."
            }
        },
        {
            ask: {
                choices: {
                    value: "[5 DIGITS]"
                },
                attempts: 3,
                bargein: false,
                name: "foo",
                required: true,
                say: {
                    value: "Please enter your 5 digit zip code."
                },
                timeout: 10
            }
        },
        {
            on: {
                event: "continue",
                next: "/askanswer/answer",
                required: true
            }
        }
    ]
}

if path is answer?

{
    tropo: [
        {
            say: {
                value: "Your zip code is 52521, thank you!"
            }
        }
    ]
}
```

#### Voice Call

You can connect your app to also call a customer to initiate the Ask and Answer features.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Hello World")

call = voice.call("9065263453")
call.setFrom("sip:21584130@sip.tropo.net")

voice.addCall(call)
voice.addSay(say)

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            call: {
                to: "9065272450",
                from: "sip:21584130@sip.tropo.net"
            }
        },
        [
            {
                value: "Hello World"
            }
        ]
    ]
}
```

#### Voice Conference

You can take advantage of Globe's automated Ask protocols to help service your customers without manual intervention for common questions in example.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API Conference Call.")

jPrompt = voice.joinPrompt("http://openovate.com/hold-music.mp3")
lPrompt = voice.leavePrompt("http://openovate.com/hold-music.mp3")

conference = voice.conference("12345")
conference.setMute(false)
conference.setName("foo")
conference.setPlayTones(true)
conference.setTerminator("#")
conference.setJoinPrompt(jPrompt)
conference.setLeavePrompt(lPrompt)

voice.addSay(say)
voice.addConference(conference)

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API Conference Call."
        }
        },
        {
            conference: {
                id: "12345",
                mute: false,
                name: "foo",
                playTones: true,
                terminator: "#",
                joinPrompt: {
                    value: "http://openovate.com/hold-music.mp3"
                },
                leavePrompt: {
                    value: "http://openovate.com/hold-music.mp3"
                }
            }
        }
    ]
}
```

#### Voice Event

Call events are triggered depending on the response of the receiving person. Events are used with the Ask and Answer features.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

e1 = voice.say("sorry, I did not hear anything.")
e1.setEvent("timeout")

e2 = voice.say("sorry, that was not a valid option.")
e2.setEvent("nomatch:1")

e3 = voice.say("Nope, still not a valid response.")
e3.setEvent("nomatch:3")

say = voice.say("Welcome to my tropo web API.")
eSay = voice.say("Please enter your 5 digit zip code.")
eSay.event([e1, e2, e3]);

choices = voice.choices("[5 DIGITS]")
ask = voice.ask(eSay)
ask.setChoices(choices)
ask.setAttempts(3)
ask.setBargein(false)
ask.setName("foo")
ask.setRequired(true)
ask.setTimeout(10)

on = voice.on("continue")
on.setNext("/answer")
on.setRequired(true)

voice.addSay(say)
voice.addAsk(ask)
voice.addOn(on)

print voice.getObject()
```

##### Sample Results

```json
{
tropo: [
    {
        say: {
            value: "Welcome to my Tropo Web API."
        }
    },
    {
        ask: {
                choices: {
                    value: "[5 DIGITS]"
                },
                attempts: 3,
                bargein: false,
                name: "foo",
                required: true,
                say: [
                    {
                        value: "Sorry, I did not hear anything.",
                        event: "timeout"
                    },
                    {
                        value: "Sorry, that was not a valid option.",
                        event: "nomatch:1"
                    },
                    {
                        value: "Nope, still not a valid response",
                        event: "nomatch:2"
                    },
                    {
                        value: "Please enter your 5 digit zip code."
                    }
                ],
                timeout: 5
            }
        },
        {
            on: {
                event: "continue",
                next: "http://somefakehost:8000/",
                required: true
            }
        }
    ]
}
```

#### Voice Hangup

Between your automated dialogs (Ask and Answer) you can automatically close the voice call using this feature. 

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API, thank you")
voice.addSay(say)
voice.addHangup()

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API, thank you!"
            }
        },
        {
            hangup: { }
        }
    ]
}
```

#### Voice Record

It is helpful to sometime record conversations, for example to help improve on the automated dialog (Ask and Answer). The following sample shows how you can use connect your application with voice record features.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API.")
e1 = voice.say("Sorry, I did not hear anything. Please call back.")
e1.setEvent("timeout")

say2 = voice.say("Please leave a message")
say2.setEvent([e1])

choices = voice.choices()
choices.setTerminator("#")

transcription = voice.transcription("1234")
transcription.setUrl("mailto:charles.andacc@gmail.com")

record = voice.record("foo", "http://openovate.com/globe.php")
record.setFormat("wav")
record.setAttempts(3)
record.setBargein(false)
record.setMethod("POST")
record.setRequired(true)
record.setSay(say2)
record.setChoices(choices)
record.setTranscription(transcription)

voice.addSay(say)
voice.addRecord(record)

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API."
            }
        },
        {
            record: {
                attempts: 3,
                bargein: false,
                method: "POST",
                required: true,
                say: [
                    {
                        value: "Sorry, I did not hear anything. Please call back.",
                        event: "timeout"
                    },
                    {
                        value: "Please leave a message"
                    }
                ],
                name: "foo",
                url: "http://openovate.com/globe.php",
                format: "audio/wav",
                choices: {
                    terminator: "#"
                },
                transcription: {
                    id: "1234",
                    url: "mailto:charles.andacc@gmail.com"
                }
            }
        }
    ]
}
```

#### Voice Reject

To filter incoming calls automatically, you can use the following example below. 

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

voice.addReject()

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            reject: { }
        }
    ]
}
```

#### Voice Routing

To help integrate Globe Voice with web applications, this API using routing which can be easily routed within your framework.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

if url == "/routing":
    say = voice.say("Welcome to my Tropo Web API.")

    on = voice.on("continue")
    on.setNext("/routing1")

    voice.addSay(say)
    voice.addOn(on)
elif url == "/routing1":
    say = voice.say("Hello from resource one.")

    on = voice.on("continue")
    on.setNext("/routing2")

    voice.addSay(say)
    voice.on(on)
elif(url == "/routing2":
    say = voice.say("Hello from resource two! Thank you.")
    voice.addSay(say)


print voice.getObject()
```

##### Sample Results

```json
if path is routing?

{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API."
            }
        },
        {
            on: {
                next: "/VoiceSample/RoutingTest1",
                event: "continue"
            }
        }
    ]
}

if path is routing1?

{
    tropo: [
        {
            say: {
                value: "Hello from resource one!"
            }
        },
        {
            on: {
                next: "/VoiceSample/RoutingTest2",
                event: "continue"
            }
        }
    ]
}

if path is routing2?

{
    tropo: [
        {
            say: {
                value: "Hello from resource two! thank you."
            }
        }
    ]
}
```

#### Voice Say

The message you pass to `say` will be transformed to an automated voice.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API.")
say2 = voice.say("I will play an audio file for you, please wait.")
say3 = voice.say("http://openovate.com/tropo-rocks.mp3")

voice.addSay(say)
voice.addSay(say2)
voice.addSay(say3)

print voice.getObject()
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API."
            }
        },
        {
            say: {
                value: "I will play an audio file for you, please wait."
            }
        },
        {
            say: {
                value: "http://openovate.com/tropo-rocks.mp3"
            }
        }
    ]
}
```

#### Voice Transfer

The following sample explains the dialog needed to transfer the receiver to another phone number.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API, you are now being transfered.")

e1 = voice.say("Sorry, I did not hear anything")
e1.setEvent("timeout")

e2 = voice.say("Sorry, that was an invalid option.")
e2.setEvent("nomatch:1")

eventSay = voice.say("Please enter your 5 digit zip code.")
eventSay.setEvent([e1, e2])

choices = voice.choices("[5 DIGITS]")

ask = voice.ask(eventSay)
ask.setChoices(choices)
ask.setAttempts(3)
ask.setBargein(false)
ask.setName("foo")
ask.setRequired(true)
ask.setTimeout(10)

ringSay = voice.say("http://openovate.com/hold-music.mp3")

onRing = voice.on("ring")
onRing.setSay(ringSay);

onConnect = voice.on("connect")
onConnect.setSay(ringSay)

on = [onRing, onConnect]

var transfer = voice.transfer("9053801178")
transfer.setRingRepeat(2)
transfer.setOn(on)

voice.addSay(say)
voice.addTransfer(transfer)

print voice.getObject();
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API, you are now being transferred."
            }
        },
        {
            transfer: {
                to: "9053801178",
                ringRepeat: 2,
                on: [
                    {
                        event: "ring",
                        say: {
                            value: "http://openovate.com/hold-music.mp3"
                        }
                    },
                    {
                        event: "connect",
                        ask: {
                            choices: {
                                value: "[5 DIGITS]"
                            },
                            attempts: 3,
                            bargein: false,
                            name: "foo",
                            required: true,
                            say: [
                                {
                                    value: "Sorry, I did not hear anything.",
                                    event: "timeout"
                                },
                                {
                                    value: "Sorry, that was not a valid option.",
                                    event: "nomatch:1"
                                },
                                {
                                    value: "Nope, still not a valid response",
                                    event: "nomatch:2"
                                },
                                {
                                    value: "Please enter your 5 digit zip code."
                                }
                            ],
                            timeout: 5
                        }
                    }
                ]
            }
        }
    ]
}
```

#### Voice Transfer Whisper

TODO

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

if url == "/whisper":
    say = voice.say("Welcome to my Tropo Web API")
    askSay = voice.say("Press 1 to continue this call or any other to reject")
    choices = voice.choices("1")
    choices.setMode("DTMF")

    ask = voice.ask(askSay)
    ask.setChoices(choices)
    ask.setName("color")
    ask.setTimeout(60)

    onConnect1 = voice.on("connect")
    onConnect1.setAsk(ask)

    sayCon2 = voice.say("You are now being connected")
    onConnect2 = voice.on("connect")
    onConnect2.setSay(sayCon2)

    sayRing = voice.say("http://openovate.com/hold-music.mp3")
    onRing = voice.on("ring")
    onRing.setSay(say)

    on = [onRing, onConnect1, onConnect2]
    transfer = voice.transfer("9054799241")
    transfer.setName("foo")
    transfer.setOn(on)
    transfer.setRequired(true)
    transfer.terminator("*")

    incompleteSay = voice.say("Your are now being disconnected")
    onIncomplete = voice.on("incomplete")
    onIncomplete.setNext("/whisperIncomplete")
    onIncomplete.setSay(incompleteSay)

    voice.addSay(say)
    voice.addTransfer(transfer)
    voice.addOn(onIncomplete)

    print voice.getObject()
elif url == "/whisperIncomplete":
    voice.addHangup()

    print voice.getObject()
```

##### Sample Results

```json
if transfer whisper?

{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API, please hold while you are being transferred."
            }
        },
        {
            transfer: {
                to: "9054799241",
                name: "foo",
                on: [
                    {
                        event: "ring",
                        say: {
                            value: "http://openovate.com/hold-music.mp3"
                        }
                    },
                    {
                        event: "connect",
                        ask: {
                            choices: {
                                value: "1",
                                mode: "dtmf"
                            },
                            name: "color",
                            say: {
                                value: "Press 1 to accept this call or any other number to reject"
                            },
                            timeout: 60
                        }
                    },
                    {
                        event: "connect",
                        say: {
                            value: "You are now being connected."
                        }
                    }
                ],
                required: true,
                terminator: "*"
            }
        },
        {
            on: {
                event: "incomplete",
                next: "/transferwhisper/hangup",
                say: {
                    value: "You are now being disconnected."
                }
            }
        }
    ]
}

if hangup?

{
    tropo: [
        {
            hangup: { }
        }
    ]
}
```

#### Voice Wait

To put a receiver on hold, you can use the following sample.

##### Sample Code

```python
from globe.connect import voice

voice = voice.Voice()

say = voice.say("Welcome to my Tropo Web API.")
wait = voice.wait(5000)
wait.setAllowSignals(true)

say2 = voice.say("Thank you for waiting.")

voice.addSay(say)
voice.addWait(wait)
voice.addSay(say2)

print voice.getObjet()
```

##### Sample Results

```json
{
    tropo: [
        {
            say: {
                value: "Welcome to my Tropo Web API, please wait for a while."
            }
        },
        {
            wait: {
                milliseconds: 5000,
                allowSignals: true
            }
        },
        {
            say: {
                value: "Thank you for waiting!"
            }
        }
    ]
}
```

### USSD

#### Overview

USSD are basic features built on most smart phones which allows the phone owner to interact with menu item choices.

#### USSD Sending

The following example shows how to send a USSD request.

##### Sample Code

```python
from globe.connect import ussd

ussd = ussd.Ussd("[token]", "[shortcode]")
ussd.setAddress("[address]")
ussd.setMessage("[message]")
ussd.setFlash("[flash]")
ussd.sendUsssdRequest()

print ussd.getResponse()
```

##### Sample Results

```json
{
    "outboundUSSDMessageRequest": {
        "address": "639954895489",
        "deliveryInfoList": {
            "deliveryInfo": [],
            "resourceURL": "https://devapi.globelabs.com.ph/ussd/v1/outbound/21589996/reply/requests?access_token=access_token"
        },
        "senderAddress": "21580001",
        "outboundUSSDMessage": {
            "message": "Simple USSD Message\nOption - 1\nOption - 2"
        },
        "receiptRequest": {
            "ussdNotifyURL": "http://example.com/notify",
            "sessionID": "012345678912"
        },
        "resourceURL": "https://devapi.globelabs.com.ph/ussd/v1/outbound/21589996/reply/requests?access_token=access_token"
    }
}
```

#### USSD Replying

The following example shows how to send a USSD reply.

##### Sample Code

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

##### Sample Results

```json
{
    "outboundUSSDMessageRequest": {
        "address": "639954895489",
        "deliveryInfoList": {
            "deliveryInfo": [],
            "resourceURL": "https://devapi.globelabs.com.ph/ussd/v1/outbound/21589996/reply/requests?access_token=access_token"
        },
        "senderAddress": "21580001",
        "outboundUSSDMessage": {
            "message": "Simple USSD Message\nOption - 1\nOption - 2"
        },
        "receiptRequest": {
            "ussdNotifyURL": "http://example.com/notify",
            "sessionID": "012345678912",
            "referenceID": "f7b61b82054e4b5e"
        },
        "resourceURL": "https://devapi.globelabs.com.ph/ussd/v1/outbound/21589996/reply/requests?access_token=access_token"
    }
}
```

### Payment

#### Overview

Your application can monetize services from customer's phone load by sending a payment request to the customer, in which they can opt to accept.

#### Payment Requests

The following example shows how you can request for a payment from a customer.

##### Sample Code

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

##### Sample Results

```json
{
    "amountTransaction":
    {
        "endUserId": "9171234567",
        "paymentAmount":
        {
            "chargingInformation":
            {
                "amount": "0.00",
                "currency": "PHP",
                "description": "my application"
            },
            "totalAmountCharged": "0.00"
        },
        "referenceCode": "12341000023",
        "serverReferenceCode": "528f5369b390e16a62000006",
        "resourceURL": null
    }
}
```

#### Payment Last Reference

The following example shows how you can get the last reference of payment.

##### Sample Code

```python
from globe.connect import payment

payment = payment.Payment("[token]")
payment.setAppKey("[app_key]")
payment.setAppSecret("[app_secret]")
payment.getLastReferenceCode()

print payment.getResponse()
```

##### Sample Results

```json
{
    "referenceCode": "12341000005",
    "status": "SUCCESS",
    "shortcode": "21581234"
}
```

### Amax

#### Overview

Amax is an automated promo builder you can use with your app to award customers with certain globe perks.

#### Sample Code

```python
from globe.connect import amax

amax = amax.Amax("[app_id]", "[app_secret]")
amax.setAddress("[address]")
amax.setToken("[token]")
amax.setPromo("[promo]")
amax.sendReward()

print amax.getResponse()
```

#### Sample Results

```json
{
    "outboundRewardRequest": {
        "transaction_id": 566,
        "status": "Please check your AMAX URL for status",
        "address": "9065272450",
        "promo": "FREE10MB"
    }
}
```

### Location

#### Overview

To determine a general area (lat,lng) of your customers you can utilize this feature.

#### Sample Code

```python
from globe.connect import location

loc = location.Location("[token]")
loc.setAddress("[address]")
loc.setRequestedAccuracy("[accuracy]")
loc.getLocation()

print loc.getResponse()
```

#### Sample Results

```json
{
    "terminalLocationList": {
        "terminalLocation": {
            "address": "tel:9171234567",
            "currentLocation": {
                "accuracy": 100,
                "latitude": "14.5609722",
                "longitude": "121.0193394",
                "map_url": "http://maps.google.com/maps?z=17&t=m&q=loc:14.5609722+121.0193394",
                "timestamp": "Fri Jun 06 2014 09:25:15 GMT+0000 (UTC)"
            },
            "locationRetrievalStatus": "Retrieved"
        }
    }
}
```

### Subscriber

#### Overview

TODO

#### Subscriber Balance

The following example shows how you can get the subscriber balance.

##### Sample Code

```python
from globe.connect import subscriber

subscriber = subscriber.Subscriber("[token]")
subscriber.setAddress("[address]")
subscriber.getSubscriberBalance()

print subscriber.getResponse()
```

##### Sample Results

```json
{
    terminalLocationList:
    {
        terminalLocation:
        [
            {
                address: "639171234567",
                subBalance: "60200"
            }
        ]
    }
}
```

#### Subscriber Reload

The following example shows how you can get the subscriber reload amount.

##### Sample Code

```python
from globe.connect import subscriber

subscriber = subscriber.Subscriber("[token]")
subscriber.setAddress("[address]")
subscriber.getReloadAmount()

print subscriber.getResponse()
```

##### Sample Results

```json
{
    terminalLocationList:
    {
        terminalLocation:
        [
            {
                address: "639171234567",
                reloadAmount: "30000"
            }
        ]
    }
}
```
