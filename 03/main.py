import string

with open('input.txt') as f:
  data = [idx.strip() for idx in f]

values = '0' + string.ascii_lowercase + string.ascii_uppercase

# Part 1
intersections = []
for idx in data:
  split_data = (set(idx[:int(len(idx)/2)]), set(idx[int(len(idx)/2):]))
  intersections.append(list(split_data[0].intersection(split_data[1]))[0])

score = 0
for letter in intersections:
  score += values.index(letter)
print(score)

# Part 2
def chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

score = 0
for group in chunks(data, 3):
  score += values.index(
    list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
  )
print(score)