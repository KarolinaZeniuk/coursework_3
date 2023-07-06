from function import *
import json


content = get_json()
last_five_operation = find_last_five(content)
last_five = show_last_five(last_five_operation)
for i in last_five:
    print(i)
    print("------")












