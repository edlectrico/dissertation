#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np


#define some data
x = [1]
pc_mean = [0.946] 
s3mini_mean = [2.764] 
s3_mean = [1.649] 
nexus10_mean = [5.147] 

#error data
pc_error = [0.017]
s3mini_error = [0.127]
s3_error = [0.076]
nexus10_error = [0.205]

ind = np.arange(1)  # the x locations for the groups
width = 0.25        # the width of the bars

fig, ax = plt.subplots()
#plot data
rects1 = ax.bar(ind, pc_mean, width, color='r', yerr=pc_error)
rects2 = ax.bar(ind+width, s3mini_mean, width, color='g', yerr=s3mini_error)
rects3 = ax.bar(ind+width+width, s3_mean, width, color='g', yerr=s3_error)
rects4 = ax.bar(ind+width+width+width, nexus10_mean, width, color='g', yerr=nexus10_error)

#configure  X axes
plt.xlim(0, 4)
plt.xticks(ind+width)

#configure  Y axes
plt.ylim(0.0, 6.0)
plt.yticks([0, 1, 2, 3, 4, 5, 6])

#labels
plt.ylabel('Time (s)' + '\n')
plt.xlabel('AdaptUIOnt' + '\n')

#title
#plt.title('Resulting means by increasing the number of ABox axioms using Pellet and Pellet4Android' + '\n')

#ax.set_xticklabels( ('PC', 'SIII Mini', 'SIII', 'Nexus 10') )
ax.set_xticklabels( ('a', 'b', 'c', 'd') )
ax.legend((rects1[0], rects2[0]), ('Pellet', 'Pellet4Android'), loc='center left', bbox_to_anchor=(0.5, 1.05), fancybox=True, shadow=True)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
'''
for t, a in zip(x, pc_mean):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, s3mini_mean):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, s3_mean):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, nexus10_mean):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')
'''

#save plot
plt.savefig('pellet_default.pdf')

plt.show()
