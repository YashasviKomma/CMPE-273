import psutil
from operator import itemgetter
from itertools import groupby
list1 = []
print "\"pid\",\"laddr\",\"raddr\",\"status\""
for c in psutil.net_connections(kind='tcp'):
        if c.raddr and c.laddr:
            laddr = "%s@%s" % (c.laddr)
            raddr = "%s@%s" % (c.raddr)
            pid = "%s" % (c.pid)
            status = "%s" % (c.status)
            tup = (pid,laddr,raddr,status)
            list1.append(tup)
list1.sort(key=itemgetter(0))
group = groupby(list1, itemgetter(0))
dict={}
for key, value in group:
    dict[key]=sum(1 for _ in value)
for key1, value in sorted(dict.iteritems(), key=lambda x: x[1],reverse=True):
        for key2,items in groupby(list1, itemgetter(0)):
            if key1 == key2:
                for d in items:
                    print("\"" + key1 + "\",\"" + d[1] + "\",\"" + d[2] + "\",\"" + d[3] + "\"")

