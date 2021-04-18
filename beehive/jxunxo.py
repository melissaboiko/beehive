import json
import yaml
import re

def jxunxo(jsonstr: str) -> str:
    '''Hacky problematic/imprecise syntax for typing quick json snippets.

>>> jxunxo('color:red')
'{"color": "red"}'

>>> jxunxo('"color":"red"')
'{"color": "red"}'

>>> jxunxo('color:#ff0000,transition:2') # ew integer guessing
'{"color": "#ff0000", "transition": 2}'

>>> jxunxo('color:#ff0000')
'{"color": "#ff0000"}'

>>> jxunxo('value:false,country:no') # ew² boolean guessing
'{"value": false, "country": false}'

(It’s YAML.  It’s just YAML.)

'''
    if jsonstr[0] != '{':
        jsonstr = '{' + jsonstr + '}'
    jsonstr = re.sub(r'([^"])(#[0-9a-zA-z]{6})([^"])', r'\1"\2"\3', jsonstr)
    # yaml can't handle no space after colon
    jsonstr = re.sub(r':([^ ])', r': \1', jsonstr)
    return json.dumps(yaml.load(jsonstr))
