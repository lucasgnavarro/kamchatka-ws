import json
from kamchatka.net.status_codes import *


def simple_response(data=None, status_code=HTTP_200, message=None):
    success_status_list = (HTTP_200,)
    fail_status_list = (HTTP_400,)
    error_status_list = (HTTP_500,)
    status = None

    # Set human-readable response status
    if status_code in success_status_list:
        status = 'success'
    elif status_code in error_status_list:
        status = 'error'
    elif status_code in fail_status_list:
        status = 'fail'

    _to_return = {'status': status}
    if data is not None:
        _to_return['data'] = data

    if message is not None:
        _to_return['message'] = message

    try:
        response_body = json.dumps(_to_return)
    except Exception as e:
        response_body = json.dumps({'status': 'error', 'message': str(e)})

    return response_body