import sys
import json

class AppServerRequest():
    responseQueue = ''
    requestBody = ''
    pageIndex = 0
    pageSize = 0

    def __init__(self,responseQueue = '',requestBody = '',pageIndex = 0,pageSize = 0):
        self.responseQueue = responseQueue
        self.requestBody = requestBody
        self.pageIndex = pageIndex
        self.pageSize = pageSize
       
class AppServerRequestFactory():
    @staticmethod
    def fromJson(jsonString):
        return AppServerRequest(**json.loads(jsonString))

