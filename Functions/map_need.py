def mins_to_sec(mins):
    return mins * 60

def temp_convert(c):
    return 9/5 * c + 32

# mins = 4
# print(mins_to_sec(mins))
#
# t = 44.12
# print(temp_convert(t))

mins = [4,5,6,12,32,56,44.3,12.5]
# sec = []
# for m in mins:
#     sec.append(mins_to_sec(m))
# print(sec)
#
t = [34.5,43.3,32.5,37.8,29.7,22.6]
# f = []
# for temp in t:
#     f.append(temp_convert(temp))
# print(f)

def mymap(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

print(mymap(mins_to_sec, mins))
print(mymap(temp_convert, t))
