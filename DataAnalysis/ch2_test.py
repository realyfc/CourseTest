# 对附录中的Python语法进行考试测验

import os
import sys

sys.path.append("./test")
exec('import test4 as ta')
lf = {  # 'create_list',
    0: 'what_sign',
    1: 'fizzbuzz'}
cases = {'what_sign': {3: 'Positive', 0: 'Zero', -3: 'Negative'}
         }
for i, fn in lf.items():
    if fn in dir(ta):
        exec('f = ta.' + fn)
        print(f([10]))
        print(i, fn)


# exec('del ta')
# exec('testa = ta.create_list')
# sys.path.remove("./test")
# exec('del ta')

def walk_dir(dir, topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            ext = os.path.splitext(name)[1]
            if ext == '.py':
                pass
        pass
    pass


    #
    #
    # print(testa() == ['A', 'B', 'C'])
    # print(sys.path)
    # sys.path.append("./test")
    # print(sys.path)
    # sys.path.remove("./test")
    # print(sys.path)


t = {0, [(None, [1, 2, 3]), (None, [2, 3, 4])]}
