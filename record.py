import pdb
import threading
from threading import Thread
import datetime

sleep_second = 2
queue_size = 20480

class tickerRecord(Thread):


    
    def run(self):
        c = OKCoin()
        dt = datetime.datetime.now()
        

        f = open(str(dt),"w")
        
        for i in range(0, (6)*60*24):

            ticker = c.get_ticker("btc_cny")
            d = {k.encode('ascii') : v.encode('ascii') for (k, v) in ticker.iteritems()}
            l = [v.encode('ascii') for (k, v) in ticker.iteritems()]

            line = ', '.join(l)
            f.write(line)

            print "buy, sell, low, high, last, volumn"
            print line

            if (len(queue) >= queue_size):
                q.get()

            q.put(d)
            time.sleep(sleep_second)
        f.close()        

class analysis(Thread):
    def window(p_second, p_npoint, p_key):

        flag = True
        pos = p_second / sleep_second
        for i in range(0, p_npoint/2):
            if (q[i*pos][p_key] > q[(i+1)* pos][p_key]):
                flag = False
                break
        for j in range(p_npoint/2):
            if (q[i*pos][p_key] < q[(i+1)* pos][p_key]):
                flag = False
                break

        if (falg == False):
          #  buyobj = Buy()
        

           

        
class Operator():
    buy()
    sell()
        

if __name__ == '__main__':
#    c= OKCoin("3523330",  "ABF9356BCD703F04EA7FF83AB53826B0") ;

#    partner = ""
#    key = ""

#    pair = "btc_cny"

    analysis

    
    global q = Queue.Queue();

    
    
    t = tickerRecord()
    t.start()




    
 #    c = OKCoin();
 #     re = c.get_ticker("btc_cny");
 # #    print re

 #     print "dirct"
 #     repon = urllib2.urlopen("https://www.okcoin.com/api/ticker.do")
 #     print repon.read()
