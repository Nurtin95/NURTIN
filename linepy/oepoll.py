# -*- coding: utf-8 -*-
from .client import LINE
from types import *
from sync_service.ttypes import *
import os, sys, threading, time

class OEPoll(object):
    OpInterrupt = {}
    client = None
    __squareSubId = {}
    __squareSyncToken = {}

    def __init__(self, client):
        if type(client) is not LINE:
            raise Exception('You need to set LINE instance to initialize OEPoll')
        self.client = client
    
    def __fetchOperation(self, revision, count=1):
        return self.client.poll.fetchOperations(revision, count)
    
    def __sync(self, count=100):
        return self.client.fetch.sync(SyncRequest(
            self.client.revision, count, self.client.globalRev, self.client.individualRev,
        ))

    def __execute(self, op, threading):
        try:
            if threading:
                _td = threading.Thread(target=self.OpInterrupt[op.type](op))
                _td.daemon = False
                _td.start()
            else:
                self.OpInterrupt[op.type](op)
        except Exception as e:
            self.client.log(e)

    def addOpInterruptWithDict(self, OpInterruptDict):
        self.OpInterrupt.update(OpInterruptDict)

    def addOpInterrupt(self, OperationType, DisposeFunc):
        self.OpInterrupt[OperationType] = DisposeFunc
    
    def setRevision(self, revision):
        self.client.revision = max(revision, self.client.revision)

    def singleTrace(self, count=1):
        try:
            sync_res = self.__sync()
            if sync_res.fullSyncResponse != None:
                self.client.revision = sync_res.fullSyncResponse.nextRevision
                return None
            opss = sync_res.operationResponse
            try:self.client.globalRev = opss.globalEvents.lastRevision
            except:pass
            try:self.client.individualRev = opss.individualEvents.lastRevision
            except:pass
            operations = opss.operations
            for op in operations:
                self.setRevision(op)
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            if "TalkException" in str(e) or "shouldsync" in str(e).lower():
                sys.exit(str(e))
            #print(e)
        if operations is None:
            return None
        else:
            return operations

    def trace(self, threading=False):
        try:
            operations = self.__fetchOperation(self.client.revision)
        except KeyboardInterrupt:
            exit()
        except:
            return
        
        for op in operations:
            if op.type in self.OpInterrupt.keys():
                self.__execute(op, threading)
            self.setRevision(op.revision)

    def singleFetchSquareChat(self, squareChatMid, limit=1):
        if squareChatMid not in self.__squareSubId:
            self.__squareSubId[squareChatMid] = 0
        if squareChatMid not in self.__squareSyncToken:
            self.__squareSyncToken[squareChatMid] = ''
        
        sqcEvents = self.client.fetchSquareChatEvents(squareChatMid, subscriptionId=self.__squareSubId[squareChatMid], syncToken=self.__squareSyncToken[squareChatMid], limit=limit, direction=1)
        self.__squareSubId[squareChatMid] = sqcEvents.subscription
        self.__squareSyncToken[squareChatMid] = sqcEvents.syncToken

        return sqcEvents.events