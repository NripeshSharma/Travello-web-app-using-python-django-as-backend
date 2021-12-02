'''
HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. Although they can also be nouns, these request methods are sometimes referred as HTTP verbs. Each of them implements a different semantic, but some common features are shared by a group of them: e.g. a request method can be safe, idempotent, or cacheable.

GET
The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
HEAD
The HEAD method asks for a response identical to that of a GET request, but without the response body.
POST
The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
PUT
The PUT method replaces all current representations of the target resource with the request payload.

DELETE
The DELETE method deletes the specified resource.
CONNECT
The CONNECT method establishes a tunnel to the server identified by the target resource.

OPTIONS
The OPTIONS method is used to describe the communication options for the target resource.
TRACE
The TRACE method performs a message loop-back test along the path to the target resource.

PATCH
The PATCH method is used to apply partial modifications to a resource.
'''

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Note
# when a client sends a value it is in a form of object
# and when the server sends the value back it will be in a from of response
def home(request):
    return render(request,'home.html',{'name':'Nripesh'})

def add(request): #it will also accept the request
    
    '''
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])  #since we want our data to not been seen in the address bar we use
    POST method instead of get
    Also whenever we want to fetch the data we use GET and whenever we want to send the data we use POST 
    method
    '''
    
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    
    res = val1 + val2
    
    return render(request,'result.html', {'result': res})