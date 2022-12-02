with open('input.txt') as f:
  data = [(idx[0], idx[2]) for idx in f]

# choice (Loss, Draw, Win, Score)
rps = {
  'R':('P','R','S', 1),
  'P':('S','P','R', 2),
  'S':('R','S','P', 3),
}
conversion = {
  'A':'R', 'X':'R',
  'B':'P', 'Y':'P',
  'C':'S', 'Z':'S',
}
win_draw_loss = ['Z', 'Y', 'X']

# Part 1
score = 0
for i in data:
  p1, p2 = conversion[i[0]], conversion[i[1]]
  score += rps[p2][3]
  score += rps[p2].index(p1) * 3
print(score)

# Part 2
score = 0
for i in data:
  p1 = conversion[i[0]]
  p2 = rps[p1][win_draw_loss.index(i[1])]
  score += (2 - win_draw_loss.index(i[1])) * 3
  score += rps[p2][3]
print(score)