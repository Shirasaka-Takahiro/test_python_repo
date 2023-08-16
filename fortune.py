def get_fortune():
    from random import choice
    results = ['大吉', '吉', '小吉', '凶', '大凶', '末吉']
    return choice(results)

from fortune import *
result = get_fortune()
print("今日の運勢は...", result)

import os
print(os.__file__)