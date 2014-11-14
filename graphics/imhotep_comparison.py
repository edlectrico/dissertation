#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np

#data
x = [1, 2, 3]
cached = [1.257, 1.211, 1.175] 
no_cached = [15.125, 15.115, 15.094] 
adaptui = [1.899, 1.544, 1.213]

#error data
cached_err = [0.248, 0.180, 0.240]
no_cached_err = [0.445, 0.492, 0.501]


ind = np.arange(3)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
#plot data
rects1 = ax.bar(ind, cached, width, color='r', yerr=cached_err)
rects2 = ax.bar(ind+width, no_cached, width, color='y', yerr=no_cached_err)
rects3 = ax.bar(ind+width+width, adaptui, width, color='g')

#configure  X axes
plt.xlim(0,3)
plt.xticks(ind+width)

#configure  Y axes
plt.ylim(0.0, 20.0)
plt.yticks([0.0, 5.0, 10.0, 15.0, 20.0])

#labels
plt.ylabel('Time in seconds' + '\n')

#title
plt.title('Comparing Imhotep in mobile devices' + '\n')

ax.set_xticklabels( ('Galaxy SIII Mini', 'Galaxy S3', 'Nexus 10') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Imhotep with cache', 'Imhotep without cache', 'AdaptUI') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

for t, a in zip(x, cached):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, no_cached):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, adaptui):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

#save plot
plt.savefig('imhotep_comparison.pdf')

plt.show()
