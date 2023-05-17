# -*- coding: utf-8 -*-
"""685_plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A8BuqYgfNkJDEDmXZ3595tyMMB3NqLd7
"""

cot_incontext = {'flan-t5-small': [50.877192982456144, 49.824561403508774, 50.175438596491226, 51.578947368421055, 50.526315789473685, 50.877192982456144],

'flan-t5-base': [63.1578947368421, 63.859649122807014, 61.75438596491228, 61.05263157894737, 61.75438596491228, 61.75438596491228],

'flan-t5-large': [82.45614035087719, 81.05263157894737, 82.10526315789474, 82.10526315789474, 82.45614035087719, 81.75438596491227],

'flan-t5-xl': [88.7719298245614, 89.47368421052632, 90.17543859649123, 89.47368421052632, 90.52631578947368, 90.17543859649123],

'flan-t5-xxl': [90.52631578947368, 88.7719298245614, 89.82456140350877, 89.47368421052632, 89.82456140350877, 89.82456140350877],

'text-davinci-003': [70.52631578947368, 74.3859649122807, 71.92982456140351, 73.68421052631579, 74.73684210526316, 74.03508771929824] }

cot_random = {'flan-t5-small': [50.877192982456144, 50.526315789473685, 50.175438596491226, 49.824561403508774, 50.526315789473685, 51.2280701754386],

'flan-t5-base': [63.1578947368421, 63.50877192982456, 65.26315789473685, 64.56140350877193, 63.50877192982456, 62.807017543859644],

'flan-t5-large': [82.45614035087719, 80.35087719298247, 80.7017543859649, 81.40350877192982, 81.05263157894737, 81.05263157894737],

'flan-t5-xl': [88.7719298245614, 89.47368421052632, 90.17543859649123, 89.47368421052632, 90.52631578947368, 90.17543859649123],

'flan-t5-xxl': [90.52631578947368, 89.82456140350877, 90.52631578947368, 90.87719298245615, 90.52631578947368, 90.87719298245615],

'text-davinci-003': [70.17543859649122, 73.68421052631578, 76.49122807017544, 76.84210526315789, 76.14035087719299, 75.78947368421053]}

cot_top5 = {'flan-t5-small': [50.877192982456144, 50.526315789473685, 51.2280701754386, 51.578947368421055, 50.526315789473685, 50.877192982456144],

'flan-t5-base': [63.1578947368421, 63.50877192982456, 63.1578947368421, 61.75438596491228, 62.4561403508772, 63.1578947368421],

'flan-t5-large': [82.45614035087719, 81.05263157894737, 80.35087719298247, 80.7017543859649, 80.7017543859649, 80.7017543859649],

'flan-t5-xl': [88.7719298245614, 80.35087719298247, 82.45614035087719, 88.42105263157895, 87.71929824561403, 89.12280701754386],

'flan-t5-xxl': [90.52631578947368, 90.52631578947368, 90.87719298245615, 90.52631578947368, 90.87719298245615, 91.22807017543859],

'text-davinci-003': [68.42105263157895, 54.03508771929825, 64.33333333333333, 66.66666666666666, 67.36842105263158, 67.36842105263158]}

normal_incontext = {'flan-t5-small': [50.877192982456144, 49.122807017543856, 49.122807017543856, 49.824561403508774, 49.473684210526315, 48.771929824561404],

'flan-t5-base': [63.1578947368421, 58.94736842105262, 55.78947368421052, 55.78947368421052, 55.78947368421052, 55.08771929824562],

'flan-t5-large': [82.45614035087719, 80.7017543859649, 81.40350877192982, 81.75438596491227, 82.80701754385966, 82.10526315789474],

'flan-t5-xl': [88.7719298245614, 88.0701754385965, 86.66666666666667, 87.01754385964912, 87.36842105263159, 86.66666666666667],

'flan-t5-xxl': [90.52631578947368, 90.17543859649123, 90.17543859649123, 90.17543859649123, 90.52631578947368, 90.52631578947368],
'text-davinci-003': [60.35087719298246, 75.78947368421053, 77.89473684210526, 77.89473684210526, 77.89473684210526, 75.08771929824561]}

normal_random = {'flan-t5-small': [50.877192982456144, 51.2280701754386, 51.578947368421055, 50.526315789473685, 51.2280701754386, 50.877192982456144],

'flan-t5-base': [63.1578947368421, 61.75438596491228, 60.0, 58.59649122807018, 55.43859649122807, 56.49122807017544],

'flan-t5-large': [82.45614035087719, 81.40350877192982, 80.35087719298247, 80.35087719298247, 80.0, 81.05263157894737],

'flan-t5-xl': [88.7719298245614, 89.82456140350877, 89.82456140350877, 88.7719298245614, 89.12280701754386, 88.7719298245614],

'flan-t5-xxl': [90.52631578947368, 89.47368421052632, 90.17543859649123, 89.47368421052632, 90.17543859649123, 90.52631578947368],

'text-davinci-003': [60.70175438596491, 74.3859649122807, 76.14035087719299, 76.84210526315789, 78.24561403508771, 77.54385964912281]}

keys = ['flan-t5-small', 'flan-t5-base', 'flan-t5-large', 'flan-t5-xl', 'flan-t5-xxl', 'text-davinci-003' ]

# def return_string(shot, key):
#   _dict = { 'flan-t5-small' : f"{shot}"+"         & FLAN-T5     & \multicolumn{1}{c|}{small}        &", 
#           'flan-t5-base' : '          &       & \multicolumn{1}{c|}{base}       & ', 
#           'flan-t5-large' : '          &       & \multicolumn{1}{c|}{large}       & ', 
#           'flan-t5-xl' : '          &       & \multicolumn{1}{c|}{xl}      & ', 
#           'flan-t5-xxl' : '          &       & \multicolumn{1}{c|}{xxl}       & ', 
#           'text-davinci-003' : '          & GPT-3.5     & \multicolumn{1}{c|}{text-davinci-003}       & ' }
#   return _dict[key]

# import math
# for shot in range(6):
#   for key in keys: #\multicolumn{1}{|c}{1}
#     temp_str = return_string(shot, key)
#     temp_str += f"{'{:.2f}'.format(normal_random[key][shot])} & {'{:.2f}'.format(normal_random[key][shot])} & - & " + '\multicolumn{1}{|c}{'+ f"{'{:.2f}'.format(cot_random[key][shot])}"+ '} & ' +f"{'{:.2f}'.format(cot_incontext[key][shot])} & {'{:.2f}'.format(cot_top5[key][shot])} \\"
#     print(temp_str)
#   print('\midrule')

import matplotlib.pyplot as plt
import numpy as np

cot_incontext = {
    #'flan-t5-small': [50.877192982456144, 49.824561403508774, 50.175438596491226, 51.578947368421055, 50.526315789473685, 50.877192982456144],
    #'flan-t5-base': [63.1578947368421, 63.859649122807014, 61.75438596491228, 61.05263157894737, 61.75438596491228, 61.75438596491228],
    'flan-t5-large': [82.45614035087719, 81.05263157894737, 82.10526315789474, 82.10526315789474, 82.45614035087719, 81.75438596491227],
    'flan-t5-xl': [88.7719298245614, 89.47368421052632, 90.17543859649123, 89.47368421052632, 90.52631578947368, 90.17543859649123],
    'flan-t5-xxl': [90.52631578947368, 88.7719298245614, 89.82456140350877, 89.47368421052632, 89.82456140350877, 89.82456140350877],
    'text-davinci-003': [70.52631578947368, 74.3859649122807, 71.92982456140351, 73.68421052631579, 74.73684210526316, 74.03508771929824]
}

cot_random = {
    #'flan-t5-small': [50.877192982456144, 50.526315789473685, 50.175438596491226, 49.824561403508774, 50.526315789473685, 51.2280701754386],
    #'flan-t5-base': [63.1578947368421, 63.50877192982456, 65.26315789473685, 64.56140350877193, 63.50877192982456, 62.807017543859644],
    'flan-t5-large': [82.45614035087719, 80.35087719298247, 80.7017543859649, 81.40350877192982, 81.05263157894737, 81.05263157894737],
    'flan-t5-xl': [88.7719298245614, 89.47368421052632, 90.17543859649123, 89.47368421052632, 90.52631578947368, 90.17543859649123],
    'flan-t5-xxl': [90.52631578947368, 89.82456140350877, 90.52631578947368, 90.87719298245615, 90.52631578947368, 90.87719298245615],
    'text-davinci-003': [70.17543859649122, 73.68421052631578, 76.49122807017544, 76.84210526315789, 76.14035087719299, 75.78947368421053]
}

cot_top5 = {
    #'flan-t5-small': [50.877192982456144, 50.526315789473685, 51.2280701754386, 51.578947368421055, 50.526315789473685, 50.877192982456144],
    #'flan-t5-base': [63.1578947368421, 63.50877192982456, 63.1578947368421, 61.75438596491228, 62.4561403508772, 63.1578947368421],
    'flan-t5-large': [82.45614035087719, 81.05263157894737, 80.35087719298247, 80.7017543859649, 80.7017543859649, 80.7017543859649],
    'flan-t5-xl': [88.7719298245614, 80.35087719298247, 82.45614035087719, 88.42105263157895, 87.71929824561403, 89.12280701754386],
    'flan-t5-xxl': [90.52631578947368, 90.52631578947368, 90.87719298245615, 90.52631578947368, 90.87719298245615, 91.22807017543859],
    'text-davinci-003': [68.42105263157895, 54.03508771929825, 64.33333333333333, 66.66666666666666, 67.36842105263158, 67.36842105263158]}

# Extracting the keys from the dictionaries as legends
legends = list(cot_incontext.keys())

# Generating x-axis values (0 to 5 shots)
x = list(range(6))

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(20,10))
width = 0.15

line_colors = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink', 'navy', 'beige']
for i, legend in enumerate(legends):
    incontext_values = cot_incontext[legend]
    random_values = cot_random[legend]
    top5_values = cot_top5[legend]
    
    incontext_bars = ax.bar(x, incontext_values, width, label=f'{legend} (In Context)',) # color=bar_colors[i])
    random_bars = ax.bar([val + width for val in x], random_values, width, label=f'{legend} (Random)',) # color=bar_colors[2*i+1])
    top5_bars = ax.bar([val + 2*width for val in x], top5_values, width, label=f'{legend} (Top 5)',) # color=bar_colors[3*i+2])
    
    # Add text labels above each bar
    for bar in incontext_bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                f'{height:.1f}', ha='center', va='bottom')
    
    for bar in random_bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                f'{height:.1f}', ha='center', va='bottom')
    
    for bar in top5_bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                f'{height:.1f}', ha='center', va='bottom')
        
    # Draw lines connecting the bars with the same legend
    for j in range(len(x)-1):
        ax.plot([ x[j], x[j+1],  ], [ incontext_values[j], incontext_values[j+1], ],
                marker='o', markersize=4, linestyle='-', color=line_colors[j], alpha=0.5)
    
    for j in range(len(x)-1):
        ax.plot([ x[j], x[j+1],  ], [ random_values[j], random_values[j+1], ],
                marker='*', markersize=4, linestyle='-', color=line_colors[2*j+1], alpha=0.5)
    
    for j in range(len(x)-1):
        ax.plot([ x[j], x[j+1],  ], [ top5_values[j], top5_values[j+1], ],
                marker='+', markersize=4, linestyle='-', color=line_colors[2*j+2], alpha=0.5)



# Setting labels, title, and legend
ax.set_xlabel('Shots')
ax.set_ylabel('Exact Match Accuracy')
ax.set_title('Comparison of CoT Accuracy for different heuristics')
ax.set_xticks([val + width / 2 for val in x])
ax.set_xticklabels(['0', '1', '2', '3', '4', '5'])

handles, labels = ax.get_legend_handles_labels()
order = [0,3,6,9,1,4,7,10,2,5,8,11]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='center left', bbox_to_anchor=(1, 0.5))


#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_ylim([50, 95])

plt.show()