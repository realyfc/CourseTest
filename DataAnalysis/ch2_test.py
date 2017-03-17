# 对附录中的Python语法进行考试测验

import os
import sys

sys.path.append("./test")
exec('import test4 as ta')
lf = {  # 'create_list',
    '0': 'get_divisble_by_5'}
for i, fn in lf.items():
    if fn in dir(ta):
        exec('f = ta.' + fn)
        print(f([10]))
        print(i, fn)


# exec('del ta')
# exec('testa = ta.create_list')
# sys.path.remove("./test")
# exec('del ta')


# eval('from ' + 'test4 ' + 'import  *')

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
