'''
import sys
print(sys.path)

import pickle
hf = open("3_t.txt", 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, hf)
hf.close()

hf = open("3_t.txt", 'rb')
data = pickle.load(hf)
print(data)
hf.close()
'''

#import os
#print(os.environ)
#print(os.environ['PATH'])

#print(os.getcwd())
#print(os.system("dir"))

'''
import time
myTime = time.time();
myStrTime = time.localtime(myTime)
myAscTime = time.asctime( myStrTime )
time.sleep(5)
myCTime = time.ctime()
print( myTime )
print( myStrTime )
print( myAscTime )
print( myCTime )
print(time.strftime('%Y_%m_%d %H:%M:%S', myStrTime))
'''

'''
import calendar
calendar.prcal( 2018 )

import webbrowser
webbrowser.open("http://google.com")
'''
'''
import time
import threading

class MyThread( threading.Thread ):

    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)


for msg in ['you', 'need', 'python']:
    thr = MyThread(msg)
    thr.start()

for i in range(100):
    time.sleep(0.1)
    print(i)
    
'''

class MyCalc:
    m_input = []
    m_sum = 0
    def __init__(self, listData):
        self.m_input = listData

    def sum(self):
        for i in self.m_input:
            self.m_sum += i
        return self.m_sum

    def avg(self):
        list_size = len(self.m_input)
        return self.m_sum/list_size


if __name__ == "__main__":
    cal1 = MyCalc( [1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())

