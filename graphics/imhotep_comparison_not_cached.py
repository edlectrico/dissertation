#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np


#data
x = [1, 2, 3]
no_cached = [15.125, 15.115, 15.094] 
labels = ['Samsung Galaxy SIII Mini', 'Samsung Galaxy S3', 'Nexus 10']

#error data
no_cached_err = [0.445, 0.492, 0.501]


#plot data
p1, = plt.plot(x, no_cached, linestyle="dashed", marker="^", color="red")

#plot only errorbars
plt.errorbar(x, no_cached, yerr=no_cached_err, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(1,3)
plt.xticks([1, 2, 3])

#configure  Y axes
plt.ylim(14.0, 15.5)
plt.yticks([14.5, 15.0, 15.5])

#labels
#plt.xlabel('\n' + 'Instances')
plt.ylabel('Time in seconds' + '\n')

#title
plt.title('Running Imhotep in mobile devices (not cached data)' + '\n')

#show plot

plt.xticks(x, labels, rotation='horizontal')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)


#save plot
plt.savefig('imhotep_comparison_not_cached.pdf')

plt.show()