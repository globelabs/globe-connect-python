from globe.connect import oauth
from globe.connect import sms
from globe.connect import location
from globe.connect import payment
from globe.connect import subscriber
from globe.connect import amax
#=====================================================================================================================================================================#


""" OAUTH samples """
# oauth = oauth.Oauth("[app_id]", "[app_secret]")
# print oauth.getRedirectUrl()
# print oauth.getAccessToken("[code]")

""" SMS Samples """
# sms = sms.Sms('[shortcode]','[token]')
# send sms
# sms = sms.sendMessage("[receiver_address]", "[message]", "[correlator]")
# OR
# sms = sms.setReceiverAddress([receiver_address]).setMessage("[message]").setClientCorrelator("[correlator]").sendMessage()
# print sms.getResponse()

# send binary sms
# sms = sms.sendBinary("[address]", "[msg]", "[header]", "[encoding]")
# OR
# sms = sms.setUserDataHeader([header]).setDataEncodingScheme([encoding]).setReceiverAddress([address]).setMessage([msg]).sendBinaryMessage()
# print sms.getResponse()

""" Location Samples """
# loc = location.Location("[token]")
# print loc.getLocation("[address]", [accuracy]).getResponse()
# OR
# print loc.setAddress([address]).setRequestedAccuracy([accuracy]).getLocation().getResponse()

""" Charging Samples """
# payment = payment.Payment("[token]")
# print payment.setAmount([amount]).setDescription([desciption]).setEndUserId([number]).setReferenceCode([referenceCOde]).setTransactionOperationStatus([status]).sendPaymentRequest()
# OR
# print payment.sendPaymentRequest("[number]", "[amount]", "[description]", "[referenceCode]", "[status]").getResponse()

""" Subscriber Balance """
#subscriber = subscriber.Subscriber("JO3SpcC-AFiC461wgOxUPDmsOTc5YiMayoK1GnQcduc")
#print subscriber.getSubscriberBalance("9065272450").getResponse()
# OR
#print subscriber.setAddress([address]).getSubscriberBalance().getResponse()

amax = amax.Amax('5ozgSgeRyeHzacXo55TR65HnqoAESbAz', '3dbcd598f268268e13550c87134f8de0ec4ac1100cf0a68a2936d07fc9e2459e');
amax.setAddress('09063389509')
amax.setToken('w7hYKxrE7ooHqXNBQkP9lg')
amax.setPromo('FREE10MB')
amax.sendReward()
print amax.getResponse()


