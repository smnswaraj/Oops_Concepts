# 1. Threads
# 2. Multiprocessing
# 3. Futures
# 4. AsyncIO

from threading import Thread

# To construct a thread, we must extend the Thread class and implement the run
# method. Any code inside the run method (or that is called from within that method)
# is executed in a separate thread.
# A thread only starts running in concurrent mode when we call the start method.

# class InputReader(Thread):
#     def run(self):
#         self.line_of_text = input()
#
# print("Enter some text and press enter: ")
# thread = InputReader()
# thread.start()
# count = result = 1
# while thread.is_alive():
#     result = count * count
#     count += 1
# print("calculated squares up to {0} * {0} = {1}".format(count, result))
# print("while you typed '{}'".format(thread.line_of_text))


# --------------------------------------------------------


from threading import Thread
import json
from urllib.request import urlopen
import time
CITIES = [
'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton',
"St. John's", 'Halifax', 'Toronto', 'Charlottetown', 'Quebec City', 'Regina'
]

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
        'http://api.openweathermap.org/data/2.5/'
        'weather?q={},CA&units=metric')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']

threads = [TempGetter(c) for c in CITIES]
start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# After the 10 threads have been started, we loop over them again, calling the join()
# method on each. This method essentially says "wait for the thread to complete before
# doing anything". We call this ten times in sequence; the for loop won't exit until all
# ten threads have completed.

# GIL : Global Interpreter Lock

























