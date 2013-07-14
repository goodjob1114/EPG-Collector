import Queue
import threading 
import urllib2
import datetime
import time

q = Queue.Queue()

def consumer():
    while True:
        print q.get()

def producer(url):
    data = urllib2.urlopen(url).read()
    for line in data:
        q.put(line)


p1 = threading.Thread(target = producer, args = ['http://localhost/1'])
p1.start()

p2 = threading.Thread(target = producer, args = ['http://localhost/2'])
p2.start()

p3 = threading.Thread(target = producer, args = ['http://localhost/3'])
p3.start()

threads = []

for n in range(2):
    thread = threading.Thread(target = consumer)
    thread.start()
    threads.append(thread)

print "running ..."

# the while loop will never end
for thread in threads:
    thread.join()
