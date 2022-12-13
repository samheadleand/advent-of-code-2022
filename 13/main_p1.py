import string

with open('input.txt') as f:
  data = [i.split('\n') for i in f.read().split('\n\n')]
  for i, pair in enumerate(data):
    data[i] = [pair[0][1:-1], pair[1][1:-1]]

def fix_packet(packet):
  opened = []
  if '[' not in packet:
    return packet
  for i, str in enumerate(packet):
    if str == '[':
      opened.append(i)
    elif str == ']':
      pair = [opened.pop(), i]
      start = packet[:pair[0]]
      middle = [packet[pair[0]+1:pair[1]]]
      end = packet[pair[1]+1:]
      #print('sme', start, '--', middle, '--', end)
      packet = fix_packet(start + middle + end)
      break
  return packet

def tidy_output(packet):
  tidy_packet = []
  num = ''
  for i in packet:
    #print('packet, i', packet, i)
    if type(i) != list:
      if i in string.digits:
        num += i
      else:
        if num:
          tidy_packet.append(int(num))
          num = ''
    elif type(i) == list:
      tidy_packet.append(tidy_output(i))
  if num:
    #print(num)
    tidy_packet.append(int(num))
  return tidy_packet

# packet = list('[[10,3,[[4],0,8]],[7,6,[]]]')
# fix = fix_packet(packet)
# print(fix)
# tidy = tidy_output(fix)
# print(tidy)

new_data = []
for i in data:
  pair = []
  for j in i:
    packet = fix_packet(list(j))
    pair.append(tidy_output(packet))
  new_data.append(pair)


def packet_checker(left, right):
  for i in range(min(len(left), len(right))):
    winner = 2
    print(left[i], right[i])
    if type(left[i]) == int and type(right[i]) == int:
      print('type a')
      if left[i] < right[i]:
        return 1
      elif left[i] > right[i]:
        return 3
    elif type(left[i]) == list and type(right[i]) == list:
      print('type b')
      print('b', left[i], right[i])
      winner = packet_checker(left[i], right[i])
    elif type(left[i]) == int:
      print('type c')
      winner = packet_checker([left[i]], right[i])
    else:
      print('type d')
      print(left[i], [right[i]])
      winner = packet_checker(left[i], [right[i]])
    if winner in [1,3]:
      return winner
  if len(right) < len(left):
    print('len false')
    return 3
  elif len(right) > len(left):
    print('len true')
    return 1
  else:
    print(2)
    return 2
# for i in new_data[6]:    
#   print(i)
# print(packet_checker(new_data[5][0], new_data[5][1]))

score = 0
for i in range(len(new_data)):
  if packet_checker(new_data[i][0], new_data[i][1]) == 1:
    score += i+1
  print()
  print()
print(score)