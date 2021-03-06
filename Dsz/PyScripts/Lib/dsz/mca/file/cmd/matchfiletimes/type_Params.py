# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_CHANGE_MODIFIED = 1
PARAMS_FLAG_CHANGE_ACCESSED = 2
PARAMS_FLAG_CHANGE_CREATED = 4

class Params:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['src'] = ''
        self.__dict__['dst'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'src':
            return self.__dict__['src']
        if name == 'dst':
            return self.__dict__['dst']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'src':
            self.__dict__['src'] = value
        elif name == 'dst':
            self.__dict__['dst'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_SRC, self.__dict__['src'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DST, self.__dict__['dst'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_FLAGS)
        self.__dict__['src'] = submsg.FindString(MSG_KEY_PARAMS_SRC)
        self.__dict__['dst'] = submsg.FindString(MSG_KEY_PARAMS_DST)
        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER)
        except:
            pass