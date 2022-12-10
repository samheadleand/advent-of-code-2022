with open('input.txt') as f:
  data = [i.strip() for i in f]
  data = [
    (i.split(' ')[0], int(i.split(' ')[1]))
    if i[0] == 'a' else i
    for i in data
  ]

# Part 1 

cycles = [1]

def apply_addx(original_val, add_val):
  return [original_val, original_val+add_val]

for ins in data:
  if ins == 'noop':
    cycles.append(cycles[-1])
  else:
    cycles = cycles + apply_addx(cycles[-1], ins[1])

score = 0
for i in [20, 60, 100, 140, 180, 220]:
  new_score = i * cycles[i-1]
  score += new_score

print(score)

# Part 2
cycle_lit_cells = [[0,1,2]]

def apply_new_lit_cells(ins, cycle_lit_cells=cycle_lit_cells):
  cycle_lit_cells.append(cycle_lit_cells[-1])
  if ins != 'noop':
    cycle_lit_cells.append([x+ins[1] for x in cycle_lit_cells[-1]])
  return cycle_lit_cells

for ins in data:
  cycle_lit_cells = apply_new_lit_cells(ins)

cells = []
for i, lit_cells in enumerate(cycle_lit_cells):
  if i%40 in lit_cells:
    cells.append('#')
  else:
    cells.append(' ')

def print_pixels():
  counter = 0
  line = ''
  for i in cells:
    if counter < 39:
      line += i
      counter += 1
    else:
      print(line)
      line, counter = '', 0

print_pixels()