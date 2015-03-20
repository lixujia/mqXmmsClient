#!/usr/bin/env python

import zmq
import time
import json

from Xmms import Xmms

ctx = zmq.Context()
sock = ctx.socket(zmq.REP)
sock.bind("tcp://*:5555")

xmms = Xmms()

while True:
    req = sock.recv()

    print(req)
    cmd = json.loads(str(req))
    rsp = xmms.dealRequest(cmd)

    sock.send(bytes(json.dumps(rsp,indent = True)))
    
    
