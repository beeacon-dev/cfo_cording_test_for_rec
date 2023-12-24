import random
import time
# function that create test case
def create_test_case(input_datas, convert_input_func, collect_func):
  # input_datas_length : 10
  test_list = [[], []]
  for i in range(10):
    test_list[0].append(input_datas[i])
    ans = collect_func(*convert_input_func(input_datas[i]))
    test_list[1].append(ans)
  return test_list

# function that evaluation submited function
def eval_func(input_datas, convert_input_func, submited_func, test_case):
    start_time = time.perf_counter()
    collect = 0
    for i in range(10):
      user_ans = submited_func(*convert_input_func(input_datas[i]))
      if test_case[1][i]==user_ans:
        collect += 1
    print(f"正解率 : {collect/10*100}%")
    if collect == 10:
      print("正解")
    else:
      print("不正解")
    print(f"実行時間(秒) : {time.perf_counter()-start_time}")
    return