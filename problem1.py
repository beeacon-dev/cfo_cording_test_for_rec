# 問題1
input_datas1 = []
for i in range(10):
  a = random.randrange(-100, 101)
  b = random.randrange(a, 101)
  c = random.randrange(-100, 101)
  d = random.randrange(c, 101)
  input_datas1.append([a, b, c, d])

def problem1_convert_input_data(input_data):
  a = input_data[0]
  b = input_data[1]
  c = input_data[2]
  d = input_data[3]
  return a, b, c, d

def problem1_collect_func(a, b, c, d):
  x_y_list = []
  for x in range(a, b+1):
    for y in range(c, d+1):
      x_y_list.append(x-y)
  return max(x_y_list)

test_case1 = create_test_case(input_datas1, problem1_convert_input_data, problem1_collect_func)
eval_func(input_datas1, problem1_convert_input_data, problem1_collect_func, test_case1)