import numpy as np 
import matplotlib.pyplot as plt 

# data
a=[1,2,3,4,5,6]
b=[4,5,5,3,3,1]

#scale of whole plot
fig=plt.figure(figsize=(6,6))

#fixing x,y
plt.xlim(0,8)
plt.ylim(0,25)

#feeding data
plt.plot(a,b)

#labeling
plt.xlabel('days')
plt.ylabel('temp')
plt.title('days vs temp')
plt.suptitle('Check',y=2)

plt.show()