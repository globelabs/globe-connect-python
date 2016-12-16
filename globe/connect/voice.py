from voiceLib import ask
from voiceLib import call
from voiceLib import choices
from voiceLib import conference
from voiceLib import joinPrompt
from voiceLib import leavePrompt
from voiceLib import machineDetection
from voiceLib import message
from voiceLib import on
from voiceLib import record
from voiceLib import redirect
from voiceLib import result
from voiceLib import say
from voiceLib import session
from voiceLib import startRecording
from voiceLib import transfer
from voiceLib import wait

import json

class Voice:
    def __init__(self):
        self = self
        self.obj = {}
        self.obj['tropo'] = []

    # say factory method
    #
    # @param    instance    say     say instance
    # @return   instance    ask     ask instance
    def ask(self, say):
        return ask.Ask(say)

    # call factory method
    #
    # @param    string      to      call address
    # @return   instance    call    call instance
    def call(self, to):
        return call.Call(to)
    
    # choices factory method
    #
    # @param    string      value
    # @return   instance    choices
    def choices(self, value):
        return choices.Choices(value)
    
    # conference factory method
    #
    # @param    string      id          conference id
    # @return   instance    conference  conference instance
    def conference(self, id):
        return conference.Conference(id)

    # joinPrompt factory method
    #
    # @param    string      value
    # @return   instance    joinPrompt
    def joinPrompt(self, value):
        return joinPrompt.JoinPrompt('value')

    # leavePrompt factory method
    #
    # @param    string      value
    # @return   instance    leavePrompt
    def leavePrompt(self, value):
        return leavePrompt.LeavePrompt('value')

    # machine detection factory method
    #
    # @return   instance    machineDetection
    def machineDetection(self):
        return machineDetection.MachineDetection()

    # message factory method
    #
    # @param    instance    say     say instance
    # @param    string      to      message to
    # @return   instance    message message instance
    def message(self, say, to):
        return message.Message(say, to)

    # on factory method
    #
    # @param    string      event
    # @param    instance    say
    # @return   instance    on
    def on(self, event, say):
        return on.On(event, say)

    # record factory method
    #
    # @param    string      name
    # @param    string      url
    # @return   instance    record
    def record(self, name, url):
        return record.Record(name, url)

    # redirect factory method
    #
    # @param    string      to
    # @return   instance    redirect
    def redirect(self, to):
        return redirect.Redirect(to)

    # result factory method
    #
    # @param    string      json
    # @return   instance    result
    def result(self, json):
        return result.Result(json)

    # say factory method
    #
    # @param    string      value
    # @return   instance    say
    def say(self, value):
        return say.Say(value)

    # session factory method
    #
    # @param    string      json
    # @return   instance    session
    def session(self, json):
        return session.Session(json)

    # startRecoding factory method
    #
    # @param    string      url
    # @return   instance    startRecording
    def startRecording(self, url):
        return startRecording.StartRecording(url)

    # transfer factory method
    #
    # @param    string      to
    # @return   instance    transafer
    def transfer(self, to):
        return transfer.Transfer(to)

    # transcription factory method
    #
    # @param    string      id
    # @return   instance    transcription
    def transfer(self, uid):
        return transcription.Transcription(uid)

    # wait factory method
    #
    # @param    string      mlscnd  millisecond
    # @return   instance    wait    wait instance
    def wait(self, mlscnd):
        return wait.Wait(mlscnd)
    
    # ask object adder
    #
    # @param    instance    ask
    # @return   instance    self
    def addAsk(self, ask):
        # add ask object to tropo array
        self.obj['tropo'].append({'ask' : ask})
        return self

    # call object adder
    #
    # @param    instance    call
    # @return   instance    self
    def addCall(self, call):
        # add call object to tropo array
        self.obj['tropo'].append({'call' : call})
        return self

    # choices object adder
    #
    # @param    instance    choices
    # @return   instance    self
    def addChoices(self, choices):
        # add choices object to tropo array
        self.obj['tropo'].append({'choices' : choices})
        return self

    # conference object adder
    #
    # @param    instance    conference
    # @return   instance    self
    def addConference(self, conference):
        # add conference object to tropo array
        self.obj['tropo'].append({'conference' : conference})
        return self

    # joinPrompt object adder
    #
    # @param    instance    joinPrompt
    # @return   instance    self
    def addJoinPrompt(self, joinPrompt):
        # add joinPrompt object to tropo array
        self.obj['tropo'].append({'joinPrompt' : joinPrompt})
        return self

    # leavePrompt object adder
    #
    # @param    instance    leavePrompt
    # @return   instance    self
    def addLeavePrompt(self, leavePrompt):
        # add leavePrompt to tropo array
        self.obj['tropo'].append({'leavePrompt' : leavePrompt})
        return self

    # machineDetection object adder
    #
    # @param    instance    machineDetection
    # @return   instance    self
    def addMachineDetection(self, machineDetection):
        # add machineDetection object to tropo array
        self.obj['tropo'].append({'machineDetection' : machineDetection})
        return self
    
    # message object adder
    #
    # @param    instance    message
    # @return   instance    self
    def addMessage(self, message):
        # add message object to tropo array
        self.obj['tropo'].append({'message' : message})
        return self
    
    # on object adder
    #
    # @param    instance    on
    # @return   instance    self
    def addOn(self, on):
        # add on object to tropo array
        self.obj['tropo'].append({'on' : on})
        return self

    # record object adder
    #
    # @param    instance    record
    # @return   instance    self
    def addRecord(self, record):
        # add record object to tropo array
        self.obj['tropo'].append({'record' : record})
        return self

    # redirect object adder
    #
    # @param    instance    redirect
    # @return   instance    self
    def addRedirect(self, redirect):
        # add redirect object to tropo array
        self.obj['tropo'].append({'redirect' : redirect})
        return self

    # result object adder
    #
    # @param    instance    result
    # @param    instance    self
    def addResult(self, result):
        # add result object to tropo array
        self.obj['tropo'].append({'result' : result})
        return self

    # say object adder
    #
    # @param    instance    say
    # @param    instance    self
    def addSay(self, say):
        self.obj['tropo'].append({'say' : say})
        return self

    # session object adder
    #
    # @param    instance    session
    # @param    instance    self
    def addSession(self, session):
        self.obj['tropo'].append({'session' : session})
        return self

    # startRecording object adder
    #
    # @param    instance    startRecording
    # @param    instance    self
    def addStartRecording(self, startRecording):
        self.obj['tropo'].append({'startRecording' : startRecording})
        return self

    # transfer object adder
    #
    # @param    instance    transfer
    # @param    instance    self
    def addTransfer(self, transfer):
        self.obj['tropo'].append({'transfer' : transfer})
        return self

    # transcription object adder
    #
    # @param    instance    transcription
    # @param    instance    self
    def addTranscription(self, transcription):
        self.obj['tropo'].append({'transcription' : transcription})
        return self

    # wait object adder
    #
    # @param    instance    wait
    # @param    instance    self
    def addWait(self, wait):
        self.obj['tropo'].append({'wait' : wait})
        return self

    def getObject(self):
        # init obj object
        obj = {}
        # init tropo array
        obj['tropo'] = []
        # loop in stored objects
        for key in self.obj['tropo']:
            for k in key:
                try:
                    # check if object has getObject method
                    obj['tropo'].append({ k : key[k].getObject()})
                except:
                    # do nothing
                    obj['tropo'].append({ k : key[k]})
        
        # return obj
        return obj

