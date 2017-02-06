from yeelight import discover_bulbs, Bulb
from ask import alexa

def lambda_handler(request, context):
    ip = discover_bulbs()[0]['ip']
    metadata = {'ip' : ip} # add your own metadata to the request using key value pairs
    return alexa.route_request(request_obj, metadata)

@alexa.request('LaunchRequest')
def launch_request_handler(request):
    return alexa.create_response(message='Launch')

@alexa.request('SessionEndRequest')
def session_ended_request_handler(request, metadata):
    return alexa.create_response(message='GoodBye!')

@alexa.intent('OnIntent')
def OnIntent(request, metadata):
    bulb = Bulb(ip)
    bulb.turn_on()

@alexa.intent('OffIntent')
def OffIntent(request, metadata):
    bulb = Bulb(ip)
    bulb.turn_off()
