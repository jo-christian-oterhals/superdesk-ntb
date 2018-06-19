"""
    This macro doesn't change any content, but when executed it'll
    transfer the article to the nynorsk-API. There it will be stored
    and used for later improvements of the translation software.
"""

import requests
from requests.auth import HTTPBasicAuth

def nob_NO_publish_macro(item, **kwargs):
    r = requests.post('http://api.smalldata.no:8080/publish', data=item, timeout=(10, 30), auth=HTTPBasicAuth('superdesk', 'babel'))
    return item

name = 'Bokmal to Nynorsk Publish Macro'
label = 'Språkvask - Lagre'
callback = nob_NO_publish_macro
access_type = 'frontend'
action_type = 'direct'
