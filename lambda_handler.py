from yeelight import discover_bulbs

def lambda_function(request, context):
    print(discover_bulbs())
