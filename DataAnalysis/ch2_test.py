# 对附录中的Python语法进行考试测验

import inspect
import os
import sys

from ch2A import *

cases = {'what_sign': [3, 0, -3],
         'fizzbuzz': [3, 15, 100],
         'remove_indices': [[['a', 'b', 'c', 'd', 'e'], [0]], [['a', 'b', 'c', 'd', 'e'], [1, 2]],
                            [['a', 'b', 'c', 'd', 'e'], [1, 4]]],
         'create_sequence': [12, 100, 1000]  # ,
         # 'add_5_to_values': [[1], [1, 4, 5]]
         }

studir = os.path.join(os.getcwd(), 'test')
funnames = set(cases.keys())

# 遍历目录
for root, dirs, files in os.walk(studir, topdown=True):
    # 查找py文件
    for name in files:
        stuno, ext = os.path.splitext(name)
        # 找到后，准备导入
        if ext == '.py':
            print('==============', stuno, '=============')
            sys.path.append(root)
            exec('import ' + stuno + ' as stufun')
            # 取得该学生所写的函数名集合
            testfunc = funnames & set(dir(stufun))
            for fun in testfunc:
                print(fun)
                # 该函数所对应的输入参数
                for arg in cases[fun]:
                    print(arg)
                    # 如果有多个输入参数
                    if len(inspect.signature(eval(fun)).parameters.values()) < 2:
                        print('result: ', eval(fun)(arg) == eval('stufun.' + fun)(arg))
                    else:
                        print('result: ', eval(fun)(arg[0], arg[1]) == eval('stufun.' + fun)(arg[0], arg[1]))
            sys.path.remove(root)
            exec('del stufun')

# input('Press any key to exit!')
