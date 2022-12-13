
with open('input.txt') as f:
  data = [
    sum([int(s) for s in idx.split('\n')])
    for idx in f.read().split('\n\n')
  ]

data.sort()

print(data[-1])
print(data[-3]+data[-2]+data[-1])