import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

h3_histogram = pd.read_csv('H3_histogram.csv')
h4a_histogram = pd.read_csv('H4A_histogram.csv')
h19_histogram = pd.read_csv('H19_histogram.csv')

plt.figure(figsize = (15, 7))
plt.title('H3 heterogeneity histogram', fontsize = 20)
plt.bar(h3_histogram['value'], h3_histogram['count'], label = 'H3', color = 'dodgerblue')
plt.xlabel('Value', fontsize = 25)
plt.ylabel('Count', fontsize = 25)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(fontsize = 20)

plt.savefig('H3_histogram.png')

plt.show()

plt.figure(figsize = (15, 7))
plt.title('H4A heterogeneity histogram', fontsize = 20)
plt.bar(h4a_histogram['value'], h4a_histogram['count'], label = 'H4A', color = 'orange')
plt.xlabel('Value', fontsize = 25)
plt.ylabel('Count', fontsize = 25)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(fontsize = 20)

plt.savefig('H4A_histogram.png')

plt.show()

plt.figure(figsize = (15, 7))
plt.title('H19 heterogeneity histogram', fontsize = 20)
plt.bar(h19_histogram['value'], h19_histogram['count'], label = 'H19', color = 'green')
plt.xlabel('Value', fontsize = 25)
plt.ylabel('Count', fontsize = 25)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(fontsize = 20)

plt.savefig('H19_histogram.png')

plt.show()

plt.figure(figsize = (15, 7))
plt.title('Comparison of heterogeneity histograms', fontsize = 20)
plt.bar(h3_histogram['value'], h3_histogram['count'], label = 'H3', color = 'dodgerblue')
plt.bar(h4a_histogram['value'], h4a_histogram['count'], label = 'H4A', color = 'orange')
plt.bar(h19_histogram['value'], h19_histogram['count'], label = 'H19', color = 'green')
plt.xlabel('Value', fontsize = 25)
plt.ylabel('Count', fontsize = 25)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(fontsize = 20)

plt.savefig('histogram.png')

plt.show()