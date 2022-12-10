import itertools

with open('input.txt') as f:
  trees = [[int(tree) for tree in row.strip()] for row in f]

def apply_move(current, direction):
  return current[0]+direction[0], current[1]+direction[1]

def check_if_visable(start, current, grid):
  return grid[start[0]][start[1]] > grid[current[0]][current[1]]

def check_all_directions(start, direction, grid=trees):
  if direction[0] == -1 or direction[1] == -1:
    end = 0
  else:
    end = len(grid) - 1
  current = start
  while current[0] != end and current[1] != end:
    current = apply_move(current, direction)
    if not check_if_visable(start, current, grid):
      return False
  return True

directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
coords = itertools.product(range(len(trees)), repeat=2)

# Part 1
visable = 0
for tree in coords:
  for direction in directions:
    if check_all_directions(tree, direction):
      visable += 1
      break

print(visable)


# Part 2

def check_visability_in_direction(start_coord, direction, grid=trees):
  if direction[0] == -1 or direction[1] == -1:
    end = 0
  else:
    end = len(grid) - 1
  current_coord = start_coord
  num_trees = 0
  while current_coord[0] != end and current_coord[1] != end:
    num_trees += 1
    current_coord = apply_move(current_coord, direction)
    #print(check_if_visable(start_coord, current_coord, grid))
    if not check_if_visable(start_coord, current_coord, grid):
      return num_trees
  return num_trees

def get_tree_score(start_coord, grid=trees):
  score = 1
  for direction in directions:
    score *= check_visability_in_direction(start_coord, direction)
  return score

top_score = 0
for tree in coords:
  for direction in directions:
    top_score = max(get_tree_score(tree), top_score)
print(top_score)