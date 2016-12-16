from globe.connect import voice
#v = voice.Voice()

#ask = v.ask('asdf')
#ask.setChoices('asdf')
#print ask.getObject()

#call = v.call('to')
#print call.getObject()

#choices = v.choices('value')
#print choices.getObject()

#conference = v.conference('id')
#print conference.getObject()

#joinPrompt = v.joinPrompt('value')
#print joinPrompt.getObject()

#leavePrompt = v.leavePrompt('value')
#print leavePrompt.getObject()

#machineDetection = v.machineDetection()
#print machineDetection.getObject()

#message = v.message('say', 'to')
#print message.getObject()

#on = v.on('event', 'say')
#print on.getObject()

#record = v.record('name', 'url')
#print record.getObject()

#redirect = v.redirect('to')
#print redirect.getObject()

#result = v.result({'result' : {'foo' : 'bar'}})
#print result.getObject()

#say = v.say('value')
#say.setEvent(['hey', 'heyVal', 'foo', 'bar'])
#print say.getObject()

#session = v.session({'session' : {'foo' : 'bar'}})
#print session.getObject()

#startRecoring = v.startRecording('asdfg.com')
#print startRecoring.getObject()

#transfer = v.transfer('to')
#transfer.setName('name')
#transfer.setChoices('[5 Digit]')
#transfer.setHeaders('headers')
#print transfer.getObject()

#wait = v.wait('100')
#print wait.getObject()

#v.addAsk(ask.getObject())
#v.addChoices(choices.getObject())
#v.addWait(wait.getObject())
#print v.getObject()

voice = voice.Voice()
call = voice.call('sip:9065272450@tropo.net')
call.setFrom('9065272450')


say = voice.say('Hello Chawse')

voice.addCall(call)
voice.addSay(say)
print voice.getObject()
