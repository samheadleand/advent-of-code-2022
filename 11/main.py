import string

with open('input.txt') as f:
  monkeys = {}
  for line in f:
    if not line.strip():
      pass
    elif line[0] == 'M':
      curr_monkey = int(line.strip().split(' ')[1][:-1])
      monkeys[curr_monkey] = {}
    elif line.strip()[0] == 'S':
      monkeys[curr_monkey]['si'] = [
        int(x) for x in line.strip()[15:].split(', ')
      ]
    elif line.strip()[0] == 'O':
      monkeys[curr_monkey]['op'] = [
        int(x) if x[0] in string.digits else x
        for x in line.strip()[17:].split(' ')
      ]
    elif line.strip()[0] == 'T':
      monkeys[curr_monkey]['t'] = int(line.strip()[19:])
    elif line.strip()[3] == 't':
      monkeys[curr_monkey]['true'] = int(line.strip()[25:])
    elif line.strip()[3] == 'f':
      monkeys[curr_monkey]['false'] = int(line.strip()[26:])
  for monkey in monkeys:
    monkeys[monkey]['ins'] = 0


# def apply_monkey_ops(monkey, item_wl, with_divide=True):
#   monkey = monkeys[monkey]
#   if monkey['op'][0] == 'old' and monkey['op'][2] == 'old':
#     if monkey['op'][1] == '+':
#       new_item_wl= item_wl + item_wl
#     elif monkey['op'][1] == '*':
#       new_item_wl = item_wl * item_wl
#   else:
#     if monkey['op'][1] == '+':
#       new_item_wl = item_wl + monkey['op'][2]
#     elif monkey['op'][1] == '*':
#       new_item_wl = item_wl * monkey['op'][2]
#   if with_divide:
#     new_item_wl = int(new_item_wl/3)
#   new_monkey = monkey['true'] if new_item_wl % monkey['t'] == 0 else monkey['false']
#   return new_item_wl, new_monkey

# def inspection_round(monkeys=monkeys, with_divide=True):
#   for monkey in monkeys:
#     #print('old monkey ins', monkey, len(monkeys[monkey]['si']))
#     monkeys[monkey]['ins'] += len(monkeys[monkey]['si'])
#     for item in monkeys[monkey]['si']:
#       new_item_wl, new_monkey = apply_monkey_ops(monkey, item, with_divide)
#       #print(new_monkey)
#       monkeys[new_monkey]['si'].append(new_item_wl)
#     monkeys[monkey]['si'] = []
#   return monkeys
  
# # Part 1
# for i in range(20):
#   monkeys = inspection_round()

# ins = []
# for monkey in monkeys:
#   ins.append(monkeys[monkey]['ins'])
# ins.sort()
# print(ins[-2] * ins[-1])

all_monkey_tests = [monkeys[monkey]['t'] for monkey in monkeys]
#print(all_monkey_tests)

class Item:
  def __init__(self, number):
    self.number = number
    self.factor_remainders = {
      test:self.number % test for test in all_monkey_tests
    }

  def recalculate_remainders(self, operator, added_value):
    for i in self.factor_remainders:
      if operator == '*' and added_value == 'old':
        self.factor_remainders[i] = (
          self.factor_remainders[i] * self.factor_remainders[i]
        ) % i
      elif operator == '*':
        self.factor_remainders[i] = (
          self.factor_remainders[i] * added_value
        ) % i
      else:
        self.factor_remainders[i] = (
          self.factor_remainders[i] + added_value
        ) % i
  
  def check_divider(self, divider):
    return self.factor_remainders[divider] == 0


for monkey in monkeys:
  new_items = []
  for item in monkeys[monkey]['si']:
    new_items.append(Item(item))
  monkeys[monkey]['si'] = new_items


def inspection_round_without_divide(monkeys=monkeys):
  for monkey in monkeys:
    monkeys[monkey]['ins'] += len(monkeys[monkey]['si'])
    for item in monkeys[monkey]['si']:
      new_item, new_monkey = apply_monkey_ops_without_divide(monkey, item)
      monkeys[new_monkey]['si'].append(new_item)
    monkeys[monkey]['si'] = []
  return monkeys


def apply_monkey_ops_without_divide(monkey, item):
  monkey = monkeys[monkey]
  item.recalculate_remainders(monkey['op'][1], monkey['op'][2])
  if monkey['t'] in item.factor_remainders:
    if item.factor_remainders[monkey['t']] == 0:
      new_monkey = monkey['true']
    else:
      new_monkey = monkey['false']
  else:
    new_monkey = monkey['false']
  return item, new_monkey


for i in range(10000):
  monkeys = inspection_round_without_divide()
  ins = []
  for monkey in monkeys:
    ins.append(monkeys[monkey]['ins'])
ins.sort()
print(ins[-1] *  ins[-2])