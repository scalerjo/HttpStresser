import requests
from multiprocessing import Pool
import time
import os

Threads = 10

# # millis = int(round(time.time() * 1000))
# # time.sleep(5)
# # print (int(round(time.time() * 1000)) - millis)

URL = "https://josephscalera.com"

def WriteFile(FileName, Content):
    try:
        os.mkdir("./data")
    except:
        pass

    try:
        os.mkdir("./data/trial")
    except:
        pass
    f = open("data/trial/" + FileName + ".txt", "w")
    f.write(Content)
    f.close()

def SpamRequest(n):
    start = int(round(time.time() * 1000))

    NumRequests = 0
    for x in range(0,1000):
        r = requests.get(URL, verify=False)
        NumRequests = NumRequests + 1
        print(NumRequests)
    
    end = int(round(time.time() * 1000))
    WriteFile(str(n), str(end-start))

def IterableArray(n):
    res = []
    for x in range(1, n+1):
        res.append(x)
    return res

if __name__ == '__main__':
    with Pool(Threads) as p:
        p.map(SpamRequest, IterableArray(Threads))

