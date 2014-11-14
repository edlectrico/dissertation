#!/usr/bin/env python
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import numpy as np


#define some data
x = [32, 5032, 10032, 15032, 20032]
pc_mean = [0.946, 3.014, 3.903, 4.228, 4.539] 
s3mini_mean = [2.764, 59.412, 30.321, 86.975, 183.882] 
s3_mean = [1.649, 36.336, 16.471, 45.387, 97.151] 
nexus10_mean = [5.147, 14.171, 9.024, 17.944, 32.070] 

#error data
pc_error = [0.017, 0.034, 0.052, 0.036, 0.042]
s3mini_error = [0.127, 0.708, 0.347, 1.108, 2.101]
s3_error = [0.076, 0.668, 0.288, 0.729, 1.208]
nexus10_error = [0.205, 0.525, 0.291, 0.496, 0.588]

#plt.subplot(121)

#plot data
p1, = plt.plot(x, pc_mean, linestyle="dashed", marker="^", color="red", label="Mean for a PC")
p2, = plt.plot(x, s3mini_mean, linestyle="-", marker="^", color="blue", label="Mean for a Samsung Galaxy SIII Mini")
p3, = plt.plot(x, s3_mean, linestyle=":", marker="^", color="green", label="Mean for a Samsung Galaxy SIII")
p4, = plt.plot(x, nexus10_mean, linestyle="-", marker="^", color="orange", label="Mean for a Nexus 10")

#legend
lgd = plt.legend([p1, p2, p3, p4], ['Mean for a PC', 'Mean for a Samsung Galaxy SIII Mini', 'Mean for a Samsung Galaxy SIII', 'Mean for a Nexus 10'], bbox_to_anchor=[0.5, -0.1], 
           loc='upper center', ncol=1, borderaxespad=0.25)

#plot only errorbars
plt.errorbar(x, pc_mean, yerr=pc_error, linestyle="None", marker="None", color="green")
plt.errorbar(x, s3mini_mean, yerr=s3mini_error, linestyle="None", marker="None", color="green")
plt.errorbar(x, s3_mean, yerr=s3_error, linestyle="None", marker="None", color="green")
plt.errorbar(x, nexus10_mean, yerr=nexus10_error, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(32,20000)
plt.xticks([32, 5032, 10032, 15032, 20032])

#configure  Y axes
plt.ylim(0.0, 5.0)
plt.yticks([0.0, 50, 100, 150, 200])

#labels
plt.xlabel('\n' + 'ABox axioms')
plt.ylabel('Time in seconds' + '\n')

#title
plt.title('Increasing the number of ABox axioms using Pellet for Java in a PC' + '\n')

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

# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)

#pm = __import__('text_positions')
#print(dir(pm)) # just for fun :)

#save plot
plt.savefig('pellet_abox.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.show()
