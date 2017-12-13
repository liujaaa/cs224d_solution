
#s1 = set([ w.strip().replace(" ","") for w in open("/Users/jie/Downloads/b1").readlines()])
#s2 = set([ w.strip().replace(" ","") for w in open("/Users/jie/Downloads/b2").readlines()])
#print len(s1),len(s2),len(s1&s2)
#for line in s2-s1:
#    print line.strip()


import numpy as np
a = np.ones((3,4))
b = np.ones((4,3))

print b.sum(axis=1,keepdims=True)

x = np.array([1,2,3,4])
b = np.ones_like(x)==1
b[2] = False
print x[b]