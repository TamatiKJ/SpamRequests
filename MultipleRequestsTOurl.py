import requests
//adding threading to send multiple requests at once
import threading

url = 'http://...'

data = {
    'cc_number' : '4007000000027',
    'cc_expmonth' : '08',
    'cc_expyear' : '21',
    'cc_cvv' : '234',
}

def do_request():
    while True:
        response = request.post(url, data=data).text
        print(response)

threads = []
for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()