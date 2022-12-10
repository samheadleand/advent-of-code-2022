with open('input.txt') as f:
  instr = []
  for i in f:
    if i[2] == 'c':
      instr.append(i[2:].strip().split(' '))
    elif i[2] == 'l':
      instr.append(['ls'])
    elif i[0] == 'd':
      instr.append(i.strip().split(' '))
    else:
      instr.append(i.strip().split(' '))

def traverse_instructions(instr):
  files = {('/',):[]}
  curr_dir = []
  ins_mode = False
  for i in instr:
    ins_mode = False
    if i[0] == 'cd':
      if i[1] == '..':
        curr_dir.pop()
      elif i[1] == '/':
        curr_dir = ['/']
      else:
        curr_dir.append(i[1])
    elif i[0] == 'ls':
      ins_mode = True
      if tuple(curr_dir) not in files:
        files[tuple(curr_dir)] = []
    else:
      if i[0] == 'dir' and tuple(curr_dir+[i[1]]) not in files:
        files[tuple(curr_dir+[i[1]])] = []
        files[tuple(curr_dir)].append(i[1])
      else:
        files[tuple(curr_dir)].append((int(i[0]), i[1]))
  return files

def find_dir_size(files, dir):
  total_size = 0
  for i in files[dir]:
    if len(i) == 2:
      total_size += i[0]
    else:
      total_size += find_dir_size(files, tuple(list(dir)+[i]))
  return total_size


files = traverse_instructions(instr)

space_to_free = 30000000-(70000000-find_dir_size(files, ('/',)))
min_dis = 70000000

# Part 1
total_size = 0
for i in files:
  folder_size = find_dir_size(files, i)
  if folder_size < 100000:
    total_size += folder_size

print(total_size)

# Part 2
for i in files:
  folder_size = find_dir_size(files, i)
  if folder_size >= space_to_free and folder_size < min_dis:
    min_dis = folder_size
print(min_dis)