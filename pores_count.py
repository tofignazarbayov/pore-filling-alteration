import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

h3_raw = pd.read_csv('H3.csv')
h4a_raw = pd.read_csv('H4A.csv')
h19_raw = pd.read_csv('H19.csv')

h3 = h3_raw[300:3900]
h4a = h4a_raw[300:3900]
h19 = h19_raw[300:3900]

h3_pores_raw = pd.read_csv('H3_pores.csv')
h4a_pores_raw = pd.read_csv('H4A_pores.csv')
h19_pores_raw = pd.read_csv('H19_pores.csv')

h3_pores = h3_pores_raw[300:3900]
h4a_pores = h4a_pores_raw[300:3900]
h19_pores = h19_pores_raw[300:3900]

h3_id = np.array(h3[' '])
h4a_id = np.array(h4a[' '])
h19_id = np.array(h19[' '])

h3_length = 20
h4a_length = 20
h19_length = 20

h3_count = np.array(h3_pores['Count'])
h3_count_max = np.max(h3_count)
h3_count_max_id = h3_id[np.argmax(h3_count)]
h3_count_min = np.min(h3_count)
h3_count_min_id = h3_id[np.argmin(h3_count)]

h4a_count = np.array(h4a_pores['Count'])
h4a_count_max = np.max(h4a_count)
h4a_count_max_id = h4a_id[np.argmax(h4a_count)]
h4a_count_min = np.min(h4a_count)
h4a_count_min_id = h4a_id[np.argmin(h4a_count)]

h19_count = np.array(h19_pores['Count'])
h19_count_max = np.max(h19_count)
h19_count_max_id = h19_id[np.argmax(h19_count)]
h19_count_min = np.min(h19_count)
h19_count_min_id = h19_id[np.argmin(h19_count)]

plt.figure(figsize = (7, 15))
plt.title('Pores count vs length for H3', fontsize = 20)
plt.plot(h3_count, h3_id, label = 'Pores count vs length', color = 'dodgerblue')
plt.scatter(h3_count_max, h3_count_max_id, color = 'orange', s = 125, label = f'Max value {np.round(h3_count_max, 2)} at slice {h3_count_max_id}')
plt.hlines(y=h3_count_max_id, xmin=0, xmax=h3_count_max, linestyles = 'dashed', color = 'orange')
plt.scatter(h3_count_min, h3_count_min_id, color = 'green', s = 125, label = f'Min value {np.round(h3_count_min, 2)} at slice {h3_count_min_id}')
plt.hlines(y=h3_count_min_id, xmin=0, xmax=h3_count_min, linestyles = 'dashed', color = 'green')
plt.legend(fontsize = 15)
plt.xlim(0.95*h3_count_min, 1.05*h3_count_max)
#plt.margins(x=0)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)
plt.yticks(list(plt.yticks()[0]) + [h3_count_max_id, h3_count_min_id, len(h3_raw)])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_max_id)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_min_id)].set_color('green')
plt.ylim(0, len(h3_raw))
plt.ylabel('Slice', fontsize = 15)
plt.xlabel('Pores count', fontsize = 15)

plt.twinx()
plt.ylim(0, h3_length)
plt.yticks(list(np.linspace(0, h3_length, 5)))
plt.ylabel('Length', fontsize = 15)
h3_count_max_length = h3_count_max_id / len(h3_raw) * h3_length
h3_count_min_length = h3_count_min_id / len(h3_raw) * h3_length
plt.yticks(list(plt.yticks()[0]) + [h3_count_max_length, h3_count_min_length])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_max_length)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_min_length)].set_color('green')

plt.savefig('H3_pores_count.png')

plt.show()

plt.figure(figsize = (7, 15))
plt.title('Pores count vs length for H4A', fontsize = 20)
plt.plot(h4a_count, h4a_id, label = 'Pores count vs length', color = 'dodgerblue')
plt.scatter(h4a_count_max, h4a_count_max_id, color = 'orange', s = 125, label = f'Max value {np.round(h4a_count_max, 2)} at slice {h4a_count_max_id}')
plt.hlines(y=h4a_count_max_id, xmin=0, xmax=h4a_count_max, linestyles = 'dashed', color = 'orange')
plt.scatter(h4a_count_min, h4a_count_min_id, color = 'green', s = 125, label = f'Min value {np.round(h4a_count_min, 2)} at slice {h4a_count_min_id}')
plt.hlines(y=h4a_count_min_id, xmin=0, xmax=h4a_count_min, linestyles = 'dashed', color = 'green')
plt.legend(fontsize = 15)
plt.xlim(0.95*h4a_count_min, 1.05*h4a_count_max)
#plt.margins(x=0)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)
plt.yticks(list(plt.yticks()[0]) + [h4a_count_max_id, h4a_count_min_id, len(h4a_raw)])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_max_id)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_min_id)].set_color('green')
plt.ylim(0, len(h4a_raw))
plt.ylabel('Slice', fontsize = 15)
plt.xlabel('Pores count', fontsize = 15)

plt.twinx()
plt.ylim(0, h4a_length)
plt.yticks(list(np.linspace(0, h4a_length, 5)))
plt.ylabel('Length', fontsize = 15)
h4a_count_max_length = h4a_count_max_id / len(h4a_raw) * h4a_length
h4a_count_min_length = h4a_count_min_id / len(h4a_raw) * h4a_length
plt.yticks(list(plt.yticks()[0]) + [h4a_count_max_length, h4a_count_min_length])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_max_length)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_min_length)].set_color('green')

plt.savefig('H4A_pores_count.png')

plt.show()

plt.figure(figsize = (7, 15))
plt.title('Pores count vs length for H19', fontsize = 20)
plt.plot(h19_count, h19_id, label = 'Pores count vs length', color = 'dodgerblue')
plt.scatter(h19_count_max, h19_count_max_id, color = 'orange', s = 125, label = f'Max value {np.round(h19_count_max, 2)} at slice {h19_count_max_id}')
plt.hlines(y=h19_count_max_id, xmin=0, xmax=h19_count_max, linestyles = 'dashed', color = 'orange')
plt.scatter(h19_count_min, h19_count_min_id, color = 'green', s = 125, label = f'Min value {np.round(h19_count_min, 2)} at slice {h19_count_min_id}')
plt.hlines(y=h19_count_min_id, xmin=0, xmax=h19_count_min, linestyles = 'dashed', color = 'green')
plt.legend(fontsize = 15)
plt.xlim(0.95*h19_count_min, 1.05*h19_count_max)
#plt.margins(x=0)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)
plt.yticks(list(plt.yticks()[0]) + [h19_count_max_id, h19_count_min_id, len(h19_raw)])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_max_id)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_min_id)].set_color('green')
plt.ylim(0, len(h19_raw))
plt.ylabel('Slice', fontsize = 15)
plt.xlabel('Pores count', fontsize = 15)

plt.twinx()
plt.ylim(0, h19_length)
plt.yticks(list(np.linspace(0, h19_length, 5)))
plt.ylabel('Length', fontsize = 15)
h19_count_max_length = h19_count_max_id / len(h19_raw) * h19_length
h19_count_min_length = h19_count_min_id / len(h19_raw) * h19_length
plt.yticks(list(plt.yticks()[0]) + [h19_count_max_length, h19_count_min_length])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_max_length)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_min_length)].set_color('green')

plt.savefig('H19_pores_count.png')

plt.show()

plt.figure(figsize = (25, 25))
plt.subplots_adjust(wspace=0.3)

plt.subplot(1, 3, 1)
plt.title('Pores count vs length for H3', fontsize = 20)
plt.plot(h3_count, h3_id, label = 'Pores count vs length', color = 'dodgerblue')
plt.scatter(h3_count_max, h3_count_max_id, color = 'orange', s = 125, label = f'Max value {np.round(h3_count_max, 2)} at slice {h3_count_max_id}')
plt.hlines(y=h3_count_max_id, xmin=0, xmax=h3_count_max, linestyles = 'dashed', color = 'orange')
plt.scatter(h3_count_min, h3_count_min_id, color = 'green', s = 125, label = f'Min value {np.round(h3_count_min, 2)} at slice {h3_count_min_id}')
plt.hlines(y=h3_count_min_id, xmin=0, xmax=h3_count_min, linestyles = 'dashed', color = 'green')
plt.legend(fontsize = 15)
plt.xlim(0.95*h3_count_min, 1.05*h3_count_max)
#plt.margins(x=0)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)
plt.yticks(list(plt.yticks()[0]) + [h3_count_max_id, h3_count_min_id, len(h3_raw)])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_max_id)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_min_id)].set_color('green')
plt.ylim(0, len(h3_raw))
plt.ylabel('Slice', fontsize = 15)
plt.xlabel('Pores count', fontsize = 15)

plt.twinx()
plt.ylim(0, h3_length)
plt.yticks(list(np.linspace(0, h3_length, 5)))
plt.ylabel('Length', fontsize = 15)
h3_count_max_length = h3_count_max_id / len(h3_raw) * h3_length
h3_count_min_length = h3_count_min_id / len(h3_raw) * h3_length
plt.yticks(list(plt.yticks()[0]) + [h3_count_max_length, h3_count_min_length])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_max_length)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h3_count_min_length)].set_color('green')

plt.subplot(1, 3, 2)
plt.title('Pores count vs length for H4A', fontsize = 20)
plt.plot(h4a_count, h4a_id, label = 'Pores count vs length', color = 'dodgerblue')
plt.scatter(h4a_count_max, h4a_count_max_id, color = 'orange', s = 125, label = f'Max value {np.round(h4a_count_max, 2)} at slice {h4a_count_max_id}')
plt.hlines(y=h4a_count_max_id, xmin=0, xmax=h4a_count_max, linestyles = 'dashed', color = 'orange')
plt.scatter(h4a_count_min, h4a_count_min_id, color = 'green', s = 125, label = f'Min value {np.round(h4a_count_min, 2)} at slice {h4a_count_min_id}')
plt.hlines(y=h4a_count_min_id, xmin=0, xmax=h4a_count_min, linestyles = 'dashed', color = 'green')
plt.legend(fontsize = 15)
plt.xlim(0.95*h4a_count_min, 1.05*h4a_count_max)
#plt.margins(x=0)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)
plt.yticks(list(plt.yticks()[0]) + [h4a_count_max_id, h4a_count_min_id, len(h4a_raw)])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_max_id)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_min_id)].set_color('green')
plt.ylim(0, len(h4a_raw))
plt.ylabel('Slice', fontsize = 15)
plt.xlabel('Pores count', fontsize = 15)

plt.twinx()
plt.ylim(0, h4a_length)
plt.yticks(list(np.linspace(0, h4a_length, 5)))
plt.ylabel('Length', fontsize = 15)
h4a_count_max_length = h4a_count_max_id / len(h4a_raw) * h4a_length
h4a_count_min_length = h4a_count_min_id / len(h4a_raw) * h4a_length
plt.yticks(list(plt.yticks()[0]) + [h4a_count_max_length, h4a_count_min_length])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_max_length)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h4a_count_min_length)].set_color('green')

plt.subplot(1, 3, 3)
plt.title('Pores count vs length for H19', fontsize = 20)
plt.plot(h19_count, h19_id, label = 'Pores count vs length', color = 'dodgerblue')
plt.scatter(h19_count_max, h19_count_max_id, color = 'orange', s = 125, label = f'Max value {np.round(h19_count_max, 2)} at slice {h19_count_max_id}')
plt.hlines(y=h19_count_max_id, xmin=0, xmax=h19_count_max, linestyles = 'dashed', color = 'orange')
plt.scatter(h19_count_min, h19_count_min_id, color = 'green', s = 125, label = f'Min value {np.round(h19_count_min, 2)} at slice {h19_count_min_id}')
plt.hlines(y=h19_count_min_id, xmin=0, xmax=h19_count_min, linestyles = 'dashed', color = 'green')
plt.legend(fontsize = 15)
plt.xlim(0.95*h19_count_min, 1.05*h19_count_max)
#plt.margins(x=0)
#plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['right'].set_visible(False)
plt.yticks(list(plt.yticks()[0]) + [h19_count_max_id, h19_count_min_id, len(h19_raw)])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_max_id)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_min_id)].set_color('green')
plt.ylim(0, len(h19_raw))
plt.ylabel('Slice', fontsize = 15)
plt.xlabel('Pores count', fontsize = 15)

plt.twinx()
plt.ylim(0, h19_length)
plt.yticks(list(np.linspace(0, h19_length, 5)))
plt.ylabel('Length', fontsize = 15)
h19_count_max_length = h19_count_max_id / len(h19_raw) * h19_length
h19_count_min_length = h19_count_min_id / len(h19_raw) * h19_length
plt.yticks(list(plt.yticks()[0]) + [h19_count_max_length, h19_count_min_length])
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_max_length)].set_color('orange')
plt.gca().get_yticklabels()[list(np.array(plt.yticks())[0]).index(h19_count_min_length)].set_color('green')

plt.savefig('comparisons_pores_count.png')

plt.show()