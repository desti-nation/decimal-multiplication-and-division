# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:53:08 2019

@author: bob
"""


import random

num = 2000
weishu = [1]

def write_file(filename, data):
    with open(filename, "w") as text_file:
        for line in data:
            text_file.write("%s\n" % line)

def get_xioashu(min = 1, max = 100):

    while(True):
        result = round(random.uniform(min, max), random.choice(weishu))
        if result % 1 == 0:
            continue
        else:
            return result
            
def get_int(min = 1, max = 100):
    return random.randint(min, max)

def get_num(min = 1, max = 100):
    if random.random() > 0.3:
        return get_int(min = min, max = max)
    else:
        return get_xioashu(min = min, max = max)

result = []
add_type = ["(x + {})", "(x - {})", "({} - x)", "({} + x)"]
count = 1


for i in range(1, num + 1):

    if (i - 1) % 10 == 0:
        result.append("=========={:04d}==========".format(count))
        count += 1

    p = random.random()
    a = get_num(min = 6, max=40)
    b = get_num(min = 6, max=40)

    if 0 <= p and p < 0.25: # +
        c = get_num(min = int(max(a, b)))
        first = "{}{}".format(a, "x" if random.random() < 0.5 else "")
        if not "x" in first:
            second = "{}".format(b)
        else:
            second = "{}{}".format(b, "x" if random.random() < 0.5 else "")
        r = "{} + {} = {}".format(first, second, c)

    elif 0.25 <= p and p < 0.5: # -
        c = get_num(max=int(min(a, b)))
        first = "{}{}".format(a, "x" if random.random() < 0.5 else "")
        if not "x" in first:
            second = "{}".format(b)
        else:
            second = "{}{}".format(b, "x" if random.random() < 0.5 else "")
        r = "{} - {} = {}".format(first, second, c)

    elif 0.5 <= p and p < 0.75: # *
        c = get_num(min=int(max(a, b)))
        first = random.choice(add_type).format(a) if random.random() < 0.5 else str(a)
        if not "x" in first:
            second = random.choice(add_type).format(b)
        else:
            second = str(b)
        r = "{} * {} = {}".format(first, second, c)

    else: # /
        c = get_num(max=int(min(a, b)))
        first = random.choice(add_type).format(a) if random.random() < 0.5 else str(a)
        if not "x" in first:
            second = random.choice(add_type).format(b)
        else:
            second = str(b)
        r = "{} / {} = {}".format(first, second, c)

    result.append(r)

write_file("result2.txt", result)

    
    