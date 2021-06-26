import numpy as np
import time
import sys

size=1000000

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()
result=[(i+j) for i,j in zip(l1,l2)]
print("List taken time: ",(time.time()-start)*1000)

start=time.time()
result=a1+a2
print("Numpy taken time: ",(time.time()-start)*1000)


