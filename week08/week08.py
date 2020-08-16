
#作业一
# list    容器序列    可变序列
# tuple   扁平序列    不可变序列
# str     扁平序列    不可变序列
# dict    容器序列    可变序列
# collection.deque    容器序列    可变序列


#作业二
def my_map(func: Callable, iterables: Iterable):
    """ 自定义一个 python 函数, 模拟 map 函数的功能 """
    if hasattr(iterables, '__iter__'):
        for i in iterables:
            yield func(i)
    else:
        raise TypeError(f"'{iterables.__class__.__name__}' object is not iterable")
        
#作业三
import time
def timer(func):
    def inner3(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        return (time.time() -start_time)
    return inner3

