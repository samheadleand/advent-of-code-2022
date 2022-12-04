with open('input.txt') as f:
  data = [[
    set(range(int(elf.split('-')[0]),int(elf.split('-')[1])+1))
           for elf in row.strip().split(',')
          ]
  for row in f
         ]

# Part 1
print(sum([pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]) for pair in data]))

# Part 2
print(sum([1 if pair[0].intersection(pair[1]) else 0 for pair in data]))