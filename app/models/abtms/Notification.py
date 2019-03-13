# encoding: utf-8

##
#   Notification
##

class Notification():
    def __init__(self, code=0, status="", owner=""):
        self.code = code
        self.status = status
        self.owner = owner
