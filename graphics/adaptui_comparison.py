#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np


#data
x = [1, 2, 3]
data = [0, 1.544, 1.213] 
labels = ['Samsung Galaxy SIII Mini', 'Samsung Galaxy S3', 'Nexus 10']

#error data
err = [0.0, 0.0, 0.0]


#plot data
p1, = plt.plot(x, data, linestyle="dashed", marker="^", color="red")

#plot only errorbars
plt.errorbar(x, data, yerr=err, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(1,3)
plt.xticks([1, 2, 3])

#configure  Y axes
plt.ylim(0.0, 3.0)
plt.yticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

#labels
#plt.xlabel('\n' + 'Instances')
plt.ylabel('Time in seconds' + '\n')

#title
plt.title('AdaptUI response to a context trigger in mobile devices' + '\n')


#show plot

plt.xticks(x, labels, rotation='horizontal')
# Pad margins so that markers don't get clipped by the axes
plt.margins(1.0)
plt.subplots_adjust(bottom=0.15)

#save plot
plt.savefig('adaptui_comparison.pdf')

plt.show()
