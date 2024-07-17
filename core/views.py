import asyncio  # Library for asynchronous programming in Python
from time import sleep  # Function for creating synchronous delays
import httpx  # Library for making HTTP requests
from django.http import HttpResponse  # Class for creating HTTP responses in Django

# Asynchronous function that makes an HTTP call and prints numbers with asynchronous delays
async def http_call_async():
    print('http_call_async')
    for num in range(1, 6):
        await asyncio.sleep(1)  # Waits 1 second asynchronously
        print(num)
    async with httpx.AsyncClient() as client:  # Creates an asynchronous HTTP client
        r = await client.get("https://httpbin.org")  # Makes an asynchronous GET request
        print(r)  # Prints the response

# Synchronous function that makes an HTTP call and prints numbers with synchronous delays
def http_call_sync():
    print('http_call_sync')
    for num in range(1, 6):
        sleep(1)  # Waits 1 second synchronously        
        print(num)
    r = httpx.get("https://httpbin.org")  # Makes a synchronous GET request
    print(r)  # Prints the response

# Asynchronous view in Django that starts the asynchronous HTTP call
async def async_view(request):
    loop = asyncio.get_event_loop()  # Gets the current asynchronous event loop
    loop.create_task(http_call_async())  # Creates an asynchronous task for http_call_async
    return HttpResponse("Non-blocking HTTP request")  # Returns an HTTP response

# Synchronous view in Django that executes the synchronous HTTP call
def sync_view(request):
    http_call_sync()  # Executes the synchronous http_call_sync function
    return HttpResponse('Blocking HTTP request')  # Returns an HTTP response
