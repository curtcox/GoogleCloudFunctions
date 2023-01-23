
def handler(request):
    haeaders =  {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'text/plain'
        }
    return (str(request), 200, haeaders)