with open('test_input.txt') as f:
  data = [idx for idx in f]
  # Tidy Stacks
  stacks_raw = [idx[:-1] for idx in data[:data.index('\n')-1][::-1]]
  stacks = [[] for i in range(int(data[data.index('\n')-1][-3]))]
  for row in stacks_raw:
    for idx in range(1, len(stacks_raw[0]), 4):
      if row[idx] != ' ':
        stacks[int((idx-1)/4)].append(row[idx])
  # Tidy moves
  moves = [
    [int(x) for x in move.strip().split(' ')[1::2]]
    for move in data[data.index('\n')+1:]
  ]

def make_move(stacks, rev, num, original, new):
  moving = stacks[original-1][-num:]
  if rev:
    moving.reverse()
  stacks[original-1] = stacks[original-1][:-num]
  stacks[new-1] = stacks[new-1] + moving
  return stacks

for move in moves:
  stacks = make_move(stacks, False, *move)

for i in stacks:
  print(i[-1])
