'''
data = [
    {},
    {},
    {}
    ]
'''

data = {
    "names" : ["John","Tom","Shawn","Harry"],
    "marks" : [67,78,88,76],
    "section" : ['A','A','B','A'],
    "hobby" : ['Football', 'Hockey', 'Hockey','Football']
    }

'''
for i in range(len(data['names'])):
    if data['hobby'][i] == 'Football':
        print(data['names'][i], ":", data['hobby'][i])
'''

for i in range(len(data['names'])):
    if data['marks'][i] >= 75:
        print(data['names'][i], ":", data['marks'][i])









