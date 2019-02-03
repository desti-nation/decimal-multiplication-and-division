# -*- coding: utf-8 -*-
"""
小学五年级上 寒假作业 小数乘除法列式计算
"""

import random

num = 200
weishu = [0, 1, 2, 3]

def write_file(filename, data):
    with open(filename, "w") as text_file:
        for line in data:
            text_file.write("%s\n" % line)

def get_xioashu():
    while(True):
        result = round(random.uniform(1, 100), random.choice(weishu))
        if result % 1 == 0:
            continue
        else:
            return result
            
def get_int():
    return random.randint(1, 100)

result =[]
count = 1
for i in range(1, num + 1):
    if (i - 1) % 5 == 0:
        result.append("=========={:04d}==========".format(count))
        count += 1
    p = random.random()
    if p <= 0.3:
        a = get_xioashu()
        b = get_int()
    elif p >= 0.3 and p < 0.9:
        a = get_xioashu()
        b = get_xioashu()
    else:
        a = get_int()
        b = get_xioashu()
    if p > 0.5:
        result.append("{} / {} = {:.4f}".format(a, b, a/b))
    else:
        result.append("{} * {} = {:.4f}".format(a, b, a*b))

write_file("result.txt", result)


