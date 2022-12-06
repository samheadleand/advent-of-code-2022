with open('input.txt') as f:
  data = f.read()

# Part 1
print(min(filter(lambda a: a != 0,
  [i+4 if len(set(data[i:i+4])) == 4 else 0 for i in range(len(data)-3)])
))

# Part 2
print(min(filter(lambda a: a != 0,
  [i+14 if len(set(data[i:i+14])) == 14 else 0 for i in range(len(data)-13)])
))