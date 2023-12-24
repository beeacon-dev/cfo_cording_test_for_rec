import random
import time
from utils import create_test_case
from utils import eval_func

# 問題2
input_datas2 = []
for i in range(10):
  N = random.randrange(1, 10**5+1)
  K = random.randrange(1, N+1)
  a = [random.randrange(1, 10**8+1) for i in range(N)]
  input_datas2.append([N, K, a])

def problem2_convert_input_data(input_data):
  N = input_data[0]
  K = input_data[1]
  a = input_data[2]
  return N, K, a

def problem2_collect_func(N, K, a):
  kernel_sum = sum(a[:K])
  ans_list = [kernel_sum]
  for i in range(K, N):
    add_data = a[i]
    kernel_sum -= a[i-K]
    kernel_sum += add_data
    ans_list.append(kernel_sum)
  return sum(ans_list)

# def problem2_collect_func(N, K, a):
#   sum_num = 0
#   for i in range(N-K+1):
#     num = sum(a[i:i+K])
#     sum_num += num
#   return sum_num

test_case2 = create_test_case(input_datas2, problem2_convert_input_data, problem2_collect_func)
eval_func(input_datas2, problem2_convert_input_data, problem2_collect_func, test_case2)