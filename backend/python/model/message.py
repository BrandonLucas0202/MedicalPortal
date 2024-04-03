"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database Message object.
"""
from model.model import Model, QueryModel

class Message(Model):
    def __init__(self, messageID) -> None:
        Model.__init__(self, "Message", [
           "messageID", "date", "time", "messageText", "senderAccountID", "recipientAccountID"
        ], {"messageID": messageID})
        self.__messageID = messageID

    def getMessageID(self):
        return self.__messageID

class OpenConversationsQuery(QueryModel):
    def __init__(self, senderAccountID) -> None:
        Model.__init__(self, "Message", [
           "DISTINCT recipientAccountID"
        ], {"senderAccountID": senderAccountID})
