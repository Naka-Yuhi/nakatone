import base64
import urllib.request
import json

class KintoneConnction:
    def __init__(self, domain, login_id, password ):
        self.__DOMAIN = domain
        self.__LOGIN_ID = login_id
        self.__PASS = password
        self.__AUTH = base64.b64encode( (f'{self.__LOGIN_ID}:{self.__PASS}').encode() )

        self.__headers_password = {
            "HOST":f'{self.__DOMAIN}.cybozu.com:443',
            "X-Cybozu-Authorization":self.__AUTH,
            "Content-Type":"application/json"
        }

    def get_record(self, app_id, record_id ):
        uri = f'https://{self.__DOMAIN}.cybozu.com/k/v1/record.json'
        body = {
            "app": app_id,
            "id": record_id
        }

        req = urllib.request.Request(
            url = uri,
            data = json.dumps(body).encode(),
            headers = self.__headers_password,
            method = "GET"
        )

        try:
            response = urllib.request.urlopen( req )
        except urllib.error.URLError as e:
            print( e )
            return {'record':'Nodata'}

        else:
            res_dict = json.load(response)
            return res_dict
        
    def get_records(self, app_id, query = '', fields = [] ):
        uri = f'https://{self.__DOMAIN}.cybozu.com/k/v1/records.json'


        body = {"app": app_id, "totalCount": True}
        if( query != ''):
            body['query'] = query
        if( len(fields) > 0  ):
            body['fields'] = fields
        
        print(body)

        req = urllib.request.Request(
            url = uri,
            data = json.dumps(body).encode(),
            headers = self.__headers_password,
            method = "GET"
        )

        try:
            response = urllib.request.urlopen( req )
        except urllib.error.URLError as e:
            print( e )
            return {'record':'Nodata'}

        else:
            res_dict = json.load(response)
            return res_dict
    def set_record(self, app_id, record ):

        uri = f'https://{self.__DOMAIN}.cybozu.com/k/v1/record.json'

        body = {
            "app": app_id,
            "record": record
        }

        req = urllib.request.Request(
            url = uri,
            data = json.dumps(body).encode(),
            headers = self.__headers_password,
            method = "POST"
        )

        try:
            response = urllib.request.urlopen( req )
        except urllib.error.URLError as e:
            print( e )
            return {'record':'Nodata'}

        else:
            res_dict = json.load(response)
            return res_dict
        
    def set_records(self, app_id, records ):
        uri = f'https://{self.__DOMAIN}.cybozu.com/k/v1/records.json'

        body = {
            "app": app_id,
            "records": records
        }

        req = urllib.request.Request(
            url = uri,
            data = json.dumps(body).encode(),
            headers = self.__headers_password,
            method = "POST"
        )
        
        try:
            response = urllib.request.urlopen( req )
        except urllib.error.URLError as e:
            print( e )
            return {'record':'Nodata'}

        else:
            res_dict = json.load(response)
            return res_dict
    def delete_records(self, app_id, record_ids ):
        uri = f'https://{self.__DOMAIN}.cybozu.com/k/v1/records.json'

        body = {
            "app": app_id,
            "ids": record_ids
        }

        req = urllib.request.Request(
            url = uri,
            data = json.dumps(body).encode(),
            headers = self.__headers_password,
            method = "DELETE"
        )

        try:
            response = urllib.request.urlopen( req )
        except urllib.error.URLError as e:
            print( e )
            return {'record':'Nodata'}

        else:
            res_dict = json.load(response)
            return res_dict