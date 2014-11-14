#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np

#data
x = [1, 2, 3, 4]
#define some data
#x = [1, 2, 3, 4, 5]
pellet4java = [1.491, 1.628, 3.502, 5.285] 
pellet4android = [1.646, 4.968, 7.597, 13.590] 

#error data
pellet4java_error = [0, 0, 0, 0]
pellet4android_error = [0, 0, 0, 0]


ind = np.arange(4)  # the x locations for the groups
width = 0.45       # the width of the bars

fig, ax = plt.subplots()
#plot data
rects1 = ax.bar(ind, pellet4java, width, color='r', yerr=pellet4java_error)
rects2 = ax.bar(ind+width, pellet4android, width, color='g', yerr=pellet4android_error)

#configure  X axes
plt.xlim(0,4)
plt.xticks(ind+width)

#configure  Y axes
plt.ylim(0.0, 15)
plt.yticks([0.0, 5, 10, 15])

#labels
plt.ylabel('Time in seconds' + '\n')
plt.xlabel('Number of rules' + '\n')

#title
#plt.title('Resulting means by increasing the number of ABox axioms using Pellet and Pellet4Android' + '\n')

ax.set_xticklabels( ('Default', '100', '500', '1,000') )
ax.legend( (rects1[0], rects2[0]), ('Pellet for Java', 'Pellet4Android') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

for t, a in zip(x, pellet4java):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')

for t, a in zip(x, pellet4android):
    plt.plot([t], [a], 'b',)
    plt.annotate(round(a, 3), xy=(t, a), xytext=(t + 0.01, a + 0.01), color='black')


#save plot
plt.savefig('reasoning_comparison.pdf')

plt.show()
