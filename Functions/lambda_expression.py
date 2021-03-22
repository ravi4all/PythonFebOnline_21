mins = [4,5,6,12,32,56,44.3,12.5]
t = [34.5,43.3,32.5,37.8,29.7,22.6]

print(list(map(lambda mins : mins * 60, mins)))
print(list(map(lambda c : 9/5 * c + 32, t)))
