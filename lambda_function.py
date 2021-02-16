from datetime import datetime
import json

import signer

def lambda_handler(event, context):

    # Try and product return a signed URL using the post data

    try:        
        request_body = json.loads(event["body"])        
        if not {'url', 'expiry', 'keyid'} <= request_body.keys():
            raise Exception()        
    except Exception as e:       
        print(e)
        return {
            'statusCode': 400,
            'body': "Bad Request"
        }

    try:
        expiry_date = datetime.strptime(request_body['expiry'], '%Y-%m-%d %H:%M:%S %Z')
        return signer.sign_url(request_body['url'], expiry_date, request_body['keyid'])
    except Exception as e:       
        print(e)
        return {
            'statusCode': 500,
            'body': "Error Signing URL"
        }

#test_json = '{"url":"https://abcd.com","expiry":"2020-01-01 00:00:00 UTC", "keyid":"blah"}'
#print(lambda_handler({'body':test_json}, None))