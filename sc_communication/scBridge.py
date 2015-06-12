import OSC


def setBassBuffer(i):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/bassSwap")
    oscmsg.append(i)
    c.send(oscmsg)


def setMelBuffer(i):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/melSwap")
    oscmsg.append(i)
    c.send(oscmsg)


def setDrumBuffer(i):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/drumSwap")
    oscmsg.append(i)
    c.send(oscmsg)


def stop():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/stop")
    c.send(oscmsg)


def play():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/play")
    c.send(oscmsg)


def makeSampler():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/makeSampler")
    c.send(oscmsg)


def loadSample(i):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/loadSample")
    oscmsg.append(i)
    c.send(oscmsg)


def panic():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/panic")
    c.send(oscmsg)


def armRecord():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/armRecord")
    c.send(oscmsg)


def beginRecord():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/beginRecord")
    c.send(oscmsg)


def stopRecord():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/stopRecord")
    c.send(oscmsg)


def quitSc():
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/quit")
    c.send(oscmsg)


def scSpeak(word, pitch):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))   # connect to SuperCollider
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/speakLyric")
    oscmsg.append(str(word))
    oscmsg.append(pitch)
    print "SPEAK!"
    c.send(oscmsg)
