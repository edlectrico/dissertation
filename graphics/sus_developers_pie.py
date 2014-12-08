from pylab import *
import matplotlib.pyplot as plt

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = ['SUS punctuation under 50 points', 'SUS punctuation between 50 and 70 points', 'SUS punctuation over or equal 70 points']
fracs = [0, 16.66666667, 75]
explode=(0.05, 0.05, 0.05)
colors = ['yellowgreen', 'gold', 'lightskyblue']

patches = pie(fracs, explode=explode, autopct='%1.1f%%', colors=colors, startangle=90)
#, texts = 
#title('SUS reponses', bbox={'facecolor':'0.8', 'pad':5})
#plt.legend(patches, labels, loc="best")

#plt.pie(sizes, colors=colors, shadow=True)
plt.axis('equal')
plt.legend(labels, loc=(-0.1, -0.1), shadow=False)
#plt.savefig(name)

plt.savefig('sus_developers.pdf')

show()

