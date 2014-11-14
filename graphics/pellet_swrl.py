#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np


#define some data
x = [13, 5013, 10013, 15013, 20013]

pc_mean = [0.105, 4.770, 6.327, 7.427, 8.147] 
s3mini_mean = [2.764, 0, 0, 0, 0] 
s3_mean = [1.649, 84.121, 74.248, 209.431, 216.005] 
nexus10_mean = [5.147, 22.317, 45.193, 85.543, 107.151] 

#error data
pc_error = [0.017, 0.141, 0.164, 0.444, 0.105]
s3mini_error = [0.127, 0,0,0,0]
s3_error = [0.076, 0.869, 0.250, 1.699, 1.202]
nexus10_error = [0.205, 0.333, 1.312, 5.490, 2.749]


#plot data
p1, = plt.plot(x, pc_mean, linestyle="dashed", marker="^", color="red", label="Mean for a PC")
p2, = plt.plot(x, s3mini_mean, linestyle="-", marker="^", color="blue", label="Mean for a Samsung Galaxy SIII Mini")
p3, = plt.plot(x, s3_mean, linestyle=":", marker="^", color="green", label="Mean for a Samsung Galaxy SIII")
p4, = plt.plot(x, nexus10_mean, linestyle="-", marker="^", color="orange", label="Mean for a Nexus 10")

#legend
lgd = plt.legend([p1, p2, p3, p4], ['Mean for a PC', 'Mean for a Samsung Galaxy SIII Mini', 'Mean for a Samsung Galaxy SIII', 'Mean for a Nexus 10'], bbox_to_anchor=[0.5, -0.1], loc='upper center', ncol=1, borderaxespad=0.25)

#plot only errorbars
plt.errorbar(x, pc_mean, yerr=pc_error, linestyle="None", marker="None", color="green")
plt.errorbar(x, s3mini_mean, yerr=s3mini_error, linestyle="None", marker="None", color="green")
plt.errorbar(x, s3_mean, yerr=s3_error, linestyle="None", marker="None", color="green")
plt.errorbar(x, nexus10_mean, yerr=nexus10_error, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(13,20013)
plt.xticks([13, 5013, 10013, 15013, 20013])

#configure  Y axes
plt.ylim(0.0, 5.0)
plt.yticks([0.0, 50, 100, 150, 200, 250])

#labels
plt.xlabel('\n' + 'SWRL axioms')
plt.ylabel('Time in seconds' + '\n')

#title
plt.title('Increasing the number of SWRL axioms' + '\n')

#show plot with data
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

#plt.xticks(x, labels, rotation='horizontal')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)


#save plot
plt.savefig('pellet_swrl.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.show()
