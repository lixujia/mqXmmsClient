import xmmsclient

class Xmms:
    def __init__(self,*args,**kargs):
        self.xmms = xmmsclient.XMMS("mqXmmsClient")
        self.xmms.connect()

    def xmmsExecute(self,func_name,*args,**kargs):
        func = getattr(self.xmms,func_name)
        res = func(*args,**kargs)
        res.wait()
        if res.iserror():
            print(res.value)
            return {"result": "ERROR"}
        
        return {"result": res.value()}

    def _checkMessage(self,msg):
        if not isinstance(msg,dict):
            raise Exception

        if not msg.has_key("func"):
            raise Exception

    def dealRequest(self,msg):
        self._checkMessage(msg)

        if msg.has_key("lst_arg"):
            lst_arg = msg["lst_arg"]
        else:
            lst_arg = []
            
        if msg.has_key("key_arg"):
            key_arg = msg["key_arg"]
        else:
            key_arg = {}
        
        return self.xmmsExecute(msg["func"],*lst_arg,**key_arg)
        
