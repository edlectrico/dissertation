#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np

#data
x = [1, 2, 3, 4]
#define some data
x = [5000, 10000, 15000, 20000]
pc_mean = [3.014, 3.903, 4.228, 4.539] 
s3mini_mean = [59.412, 30.321, 86.975, 183.882] 
s3_mean = [36.336, 16.471, 45.387, 97.151] 
nexus10_mean = [14.171, 9.024, 17.944, 32.070] 

#error data
pc_error = [0.034, 0.052, 0.036, 0.042]
s3mini_error = [0.708, 0.347, 1.108, 2.101]
s3_error = [0.668, 0.288, 0.729, 1.208]
nexus10_error = [0.525, 0.291, 0.496, 0.588]

ind = np.arange(4)  # the x locations for the groups
width = 0.15       # the width of the bars

fig, ax = plt.subplots()
#plot data
rects1 = ax.bar(ind, pc_mean, width, color='r', yerr=pc_error)
rects2 = ax.bar(ind+width, s3mini_mean, width, color='y', yerr=s3mini_error)
rects3 = ax.bar(ind+width+width, s3_mean, width, color='b', yerr=s3_error)
rects4 = ax.bar(ind+width+width+width, nexus10_mean, width, color='g', yerr=nexus10_error)

#configure  X axes
plt.xlim(0, 4)
plt.xticks(ind+width)

#configure  Y axes
plt.ylim(0.0, 200.0)
plt.yticks([0.0, 50.0, 100.0, 150.0, 200.0])

#labels
plt.ylabel('Time in seconds' + '\n')
plt.xlabel('Number of instances' + '\n')

#title
#plt.title('Resulting means by increasing the number of ABox axioms using Pellet and Pellet4Android' + '\n')

ax.set_xticklabels( ('5,000', '10,000', '15,000', '20,000') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('PC', 'Samsung Galaxy SIII Mini', 'Samsung Galaxy SIII', 'Nexus 10') )

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


#save plot
plt.savefig('pellet_abox.pdf')

plt.show()
