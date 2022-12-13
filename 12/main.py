import string

with open('input.txt') as f:
  grid = [list(i.strip()) for i in f]

def find_adj_tiles(coord, grid=grid):
  coord = list(coord)
  #print(coord)
  adj = [[coord[0]+i[0],coord[1]+i[1]] for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
  #print(adj)
  valid_adj = []
  for i in adj:
    if i[0] >= 0 and i[0] < len(grid) and i[1] >= 0 and i[1] < len(grid[0]):
      valid_adj.append(tuple(i))
  return valid_adj
  
def valid_next_move(curr_coord, next_coord, grid=grid):
  curr = grid[curr_coord[0]][curr_coord[1]]
  next = grid[next_coord[0]][next_coord[1]]
  if curr == 'S':
    curr='a'
  elif curr == 'E':
    curr = 'z'
  if next == 'S':
    next='a'
  elif next == 'E':
    next = 'z'
  return string.ascii_lowercase.index(curr)+1 >= string.ascii_lowercase.index(next)

optimal_moves = {}
recently_changed = []

def next_move(start_move=(0,0), optimal_moves=optimal_moves, grid=grid):
  recently_changed = []
  adj_tiles = find_adj_tiles(start_move)
  for i in adj_tiles:
    if valid_next_move(start_move, i):
      new_move = optimal_moves[start_move] + 1
      if i not in optimal_moves or optimal_moves[i] > new_move:
        recently_changed.append(i)
        optimal_moves[i] = new_move
  return optimal_moves, recently_changed

# Part 1

for i, row in enumerate(grid):
  if 'S' in row:
    start = (i, row.index('S'))

optimal_moves = {start:0}
recently_changed = [start]

for i, row in enumerate(grid):
  if 'E' in row:
    end = (i, row.index('E'))

while end not in optimal_moves:
  changed = []
  print(recently_changed)
  for i in recently_changed:
    optimal_moves, changed_f = next_move(start_move=i)
    changed.extend(changed_f)
  recently_changed = changed

print(optimal_moves)

# Part 2
  
possible_starts = []
for i, row in enumerate(grid):
  for j, place in enumerate(row):
    if place == 'a' or place == 'S':
      possible_starts.append((i, j))

for i, row in enumerate(grid):
  if 'E' in row:
    end = (i, row.index('E'))

times = []
for start in possible_starts:
  optimal_moves = {start:0}
  recently_changed = [start]
  while end not in optimal_moves:
    changed = []
    if not recently_changed:
      break
    for i in recently_changed:
      optimal_moves, changed_f = next_move(start_move=i, optimal_moves=optimal_moves)
      changed.extend(changed_f)
    recently_changed = changed
  if end in optimal_moves:
    times.append(optimal_moves[end])
times.sort()
print(times)