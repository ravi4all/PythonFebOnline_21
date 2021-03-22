def mins_to_sec(mins):
    return mins * 60

def temp_convert(c):
    return 9/5 * c + 32

mins = [4,5,6,12,32,56,44.3,12.5]
t = [34.5,43.3,32.5,37.8,29.7,22.6]

print(list(map(mins_to_sec, mins)))
print(list(map(temp_convert, t)))