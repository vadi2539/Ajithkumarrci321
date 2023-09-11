import logging
from flask import Request, make_response, jsonify
import zcatalyst_sdk
'''
Execute below command to install SDK in global for enabling code suggestions
-> python3 -m pip install zcatalyst-sdk
'''

def handler(request: Request):
    app = zcatalyst_sdk.initialize()
    logger = logging.getLogger()
    if request.path == "/":
        response = make_response(jsonify({
            'status': 'success',
            'message': 'Hello from main.py'
        }), 200)
        return response
    elif request.path == "/cache":
        default_segment = app.cache().segment()

        insert_resp = default_segment.put('Name', 'DefaultName')
        logger.info('Inserted cache : ' + str(insert_resp))
        get_resp = default_segment.get('Name')

        return jsonify(get_resp), 200
    else:
        response = make_response('Unknown path')
        response.status_code = 400
        return response
