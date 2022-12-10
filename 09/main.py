with open('input.txt') as f:
  moves = [[move.split(' ')[0], int(move.strip().split(' ')[1])] for move in f]

directions = {
  'R': (0, 1),
  'L': (0, -1),
  'U': (-1, 0),
  'D': (1, 0)
}

def apply_tail_move(head, tail):
  diff = (head[0] - tail[0], head[1] - tail[1])
  #print(head, tail, diff)
  if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
    return tail
  else:
    mapping = {0:0, 1:1, 2:1, -1:-1, -2:-1}
    return [tail[0] + mapping[diff[0]], tail[1] + mapping[diff[1]]]

def apply_move(head, tail, move, tail_visited):
  direction, quantity = directions[move[0]], move[1]
  for i in range(quantity):
    head = [head[0]+direction[0], head[1]+direction[1]]
    tail = apply_tail_move(head, tail)
    tail_visited.add(tuple(tail))
  return head, tail, tail_visited

# Part 1
head = [0,0]
tail = [0,0]
tail_visited = {tuple(tail)}
for move in moves:
  head, tail, tail_visited = apply_move(head, tail, move, tail_visited)
print(len(tail_visited))

# Part 2

def apply_move_multiple_tails(head, tails, move, tails_visited):
  direction, quantity = directions[move[0]], move[1]
  for i in range(quantity):
    head = [head[0]+direction[0], head[1]+direction[1]]
    tails[0] = apply_tail_move(head, tails[0])
    for i, pos in enumerate(tails[:-1]):
      tails[i+1] = apply_tail_move(tails[i], tails[i+1])
    tails_visited.add(tuple(tails[8]))
  return head, tails, tails_visited

head = [0,0]
tails = [[0, 0] for i in range(9)]
tails_visited = {(0,0)}
for move in moves:
  head, tails, tails_visited = apply_move_multiple_tails(
    head,
    tails,
    move,
    tails_visited
  )

print(len(tails_visited))