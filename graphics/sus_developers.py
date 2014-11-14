#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np

#data
x = [1]
#Developer   	Yes
minor_50 = 	[0] 
from_50_to_70 = [18.18181818] 
bigger_70 = 	[72.72727273] 

#error data
#no error data

ind = np.arange(1)  # the x locations for the groups
width = 0.20       # the width of the bars

fig, ax = plt.subplots()
#plot data
rects1 = ax.bar(ind, minor_50, width, color='g')
rects2 = ax.bar(ind+width, from_50_to_70, width, color='y')
rects3 = ax.bar(ind+width+width, bigger_70, width, color='r')

#configure  X axes
plt.xlim(0,1)
plt.xticks(ind+width)

#configure  Y axes
plt.ylim(0.0, 100.0)
plt.yticks([0.0, 25.0, 50.0, 75.0, 100.0])

#labels
plt.ylabel('% of users' + '\n')
#plt.xlabel('Developer users' + '\n')

#title
plt.title('SUS results considering users being developers' + '\n')

ax.set_xticklabels(  ('Developer users', '' ,'')  )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('<50', '>=50<x<70', '>=70') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
"""
for t, a in zip(x, minor_50):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, from_50_to_70):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, bigger_70):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')
"""
#save plot
plt.savefig('sus_developers.pdf')

plt.show()
