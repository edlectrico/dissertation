#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np

N = 4
#define some data
means = [0.946, 2.764, 1.649, 5.147] 

#error data
errors = [0.017, 0.127, 0.076, 0.205]

ind = np.arange(N)  # the x locations for the groups
width = 0.35        # the width of the bars

fig, ax = plt.subplots()
#plot data
rects1 = ax.bar(ind, means, width, color='g', yerr=errors)

#configure  X axes
plt.xlim(0, 4)
plt.xticks(ind+width)

#configure  Y axes
plt.ylim(0.0, 6.0)
plt.yticks([0, 1, 2, 3, 4, 5, 6])

#labels
plt.ylabel('Time (s)' + '\n')
plt.xlabel('Device' + '\n')

ax.set_xticklabels( ('PC', 'Samsung Galaxy SIII Mini', 'Samsung Galaxy SIII', 'Nexus 10') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)

#save plot
plt.savefig('pellet_default.pdf')

plt.show()
