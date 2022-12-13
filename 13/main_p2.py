import string

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
    tidy_packet.append(int(num))
  return tidy_packet


with open('input.txt') as f:
  data = f.read().replace('\n\n', '\n')
  data = data.split('\n')
  data = [tidy_output(fix_packet(list(i))) for i in data]


def packet_checker(left, right):
  for i in range(min(len(left), len(right))):
    winner = 2
    if type(left[i]) == int and type(right[i]) == int:
      if left[i] < right[i]:
        return 1
      elif left[i] > right[i]:
        return 3
    elif type(left[i]) == list and type(right[i]) == list:
      winner = packet_checker(left[i], right[i])
    elif type(left[i]) == int:
      winner = packet_checker([left[i]], right[i])
    else:
      winner = packet_checker(left[i], [right[i]])
    if winner in [1,3]:
      return winner
  if len(right) < len(left):
    return 3
  elif len(right) > len(left):
    return 1
  else:
    return 2

new_data = [data[0]]

for left in data[1:]:
  added = False
  for i, right in enumerate(new_data):
    if packet_checker(left, right) == 1:
      new_data = new_data[:i] + [left] + new_data[i:]
      added = True
      break
  if not added:
    new_data.append(left)

i = new_data.index([[[6]]]) + 1
j = new_data.index([[[2]]]) + 1
print(i*j)