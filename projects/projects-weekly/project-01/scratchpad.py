import csv
import numpy
data_list = []
with open('assets/sat_scores.csv', 'rU') as f: # Provide the correct path!
    reader = csv.reader(f)
    for row in reader:
        data_list.append(row)

print data_list

label_list = data_list.pop(0)
print label_list

state_names = [item for row in data_list for item in row if item == row[label_list.index('State')]]
print state_names

for item in data_list[0]:
    print type (item)

for row in data_list:
    for item in row:
        if row.index(item) > 0:
            data_list[data_list.index(row)][row.index(item)] = int(item)
print data_list

rates_list = [item for row in data_list for item in row if item == row[label_list.index('Rate')]]
verbal_list = [item for row in data_list for item in row if item == row[label_list.index('Verbal')]]
math_list = [item for row in data_list for item in row if item == row[label_list.index('Math')]]

rate_dict = {k: v for k,v in zip(state_names, rates_list)}
verbal_dict = {k: v for k,v in zip(state_names, verbal_list)}
math_dict = {k: v for k,v in zip(state_names, math_list)}
print rate_dict
print verbal_dict
print math_dict

maximum_rate = max(rate_dict, key = lambda x: rate_dict.get(x))
print(maximum_rate, rate_dict[maximum_rate])
maximum_verbal = max(verbal_dict, key = lambda x: verbal_dict.get(x))
print(maximum_verbal, verbal_dict[maximum_verbal])
maximum_math = max(math_dict, key = lambda x: math_dict.get(x))
print(maximum_math, math_dict[maximum_math])

all_lists = numpy.array([rates_list, verbal_list, math_list])
stddev = [numpy.std(item) for item in all_lists]
print stddev