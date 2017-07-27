#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


import sys
import urllib
import com.xhaus.jyson.JysonCodec as json
from xlrelease.HttpRequest import HttpRequest

SUCCES_RESULT_STATUS   = 200
RECORD_CREATED_STATUS  = 201

class RedhatSatelliteClient(object):
    def __init__(self, httpConnection, username=None, password=None): 
        self.headers        = {}
        self.query_params   = ""
        self.httpConnection = httpConnection
        if username is not None:
           self.httpConnection['username'] = username
        if password is not None:
           self.httpConnection['password'] = password
        self.httpRequest = HttpRequest(self.httpConnection, username, password)

    @staticmethod
    def create_client(httpConnection, username=None, password=None):
        return RedhatSatelliteClient(httpConnection, username, password)

    def ping(self):
        api_url = '/katello/api/v2/ping' 
        print "RedHat Satellite URL = %s " % (api_url)
        response = self.httpRequest.get(servicemanager_api_url, contentType='application/json', headers = self.headers)

        if response.getStatus() == SUCCES_RESULT_STATUS:
            data = json.loads(response.getResponse())
            return data
        else:
            print "find_record error %s" % (response)
            self.throw_error(response)
            # End if
    # End find_record        

    def throw_error(self, response):
        print "Error from RedhatSatelliteClient, HTTP Return: %s\n" % (response.getStatus())
        print "Detailed error: %s\n" % response.response
        sys.exit(1)

    def EmptyToNone(self,value):
        if value is None:
           return None
        elif value.strip() == '':
             return None
        else:
            return value
