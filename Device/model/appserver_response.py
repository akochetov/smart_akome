import sys
import json

class AppServerResponse():   
    responseBody = None
    pagesNumber = 0
    pageSize = 0
   
class AppServerResponseFactory():
    @staticmethod
    def toJson(response):
        return json.dumps(response.__dict__)
