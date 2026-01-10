import sys


def operations(k, value_dict: dict):
    if k in value_dict.keys():
        return value_dict[k], value_dict
    mod_2 = k % 2
    mod_3 = k % 3
    next_2 = (k - mod_2) // 2
    next_3 = (k - mod_3) // 3
    value_2 = operations(next_2, value_dict)[0] + mod_2 + 1
    value_3 = operations(next_3, value_dict)[0] + mod_3 + 1
    result = min(value_2, value_3)
    value_dict[k] = result
    return result, value_dict


n = int(sys.stdin.readline())
function_dict = {0: 0, 1: 0, 2: 1, 3: 1}
function_value = operations(n, function_dict)[0]
print(function_value)
