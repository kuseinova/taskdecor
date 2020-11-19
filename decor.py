# import datetime
# import time


# # 1.

# def get_func(func):
#     def wrapper():
#         time = 'datetime.now().hour'
#         if 9 <= time > 22:
#             func()
#         else:
#             print(tsh)
#     return wrapper

# @get_func
# def say_whee():
#     print("whee!")
#     return say_whee


# say_whee()


# 2.

# def timer(f):
#     def tmp():
#         start = time.time()
#         f()
#         end = time.time()
#         print('[*] Время выполнения функции: {} sec .'.format(end-start))

#     return tmp

# @timer
# def func():
#     return func
    
# func()



#3

# def repeat(num):
#     def mydec(func):
#         def wraper(*args, **kwargs):
#                 for a in range(num):
#                     func(*args, *kwargs)
#         return wraper
#     return mydec

# @repeat(num=4)
# def function(name):
#     print(name)

# function('Python')


# 4. 
# 5. 
# def myDecor(func):
#     def wrapper(a, b=1, *args, **kwargs):
#         print("Calling testFunc (", args, kwargs, ')')
#         print('argument a:', a)
#         print('argument b:', b)
#         print('argument args:', args)
#         print('argument kwargs:', kwargs)
        
        
#         print('Finished testFunc', func(a, b, *args, **kwargs))
#     return wrapper

# @myDecor
# def testFunc(a, b=1, *args, **kwargs):
#     return a + b
    
# testFunc(2, 3, 4, 5, c=6, d=7)    
# print()
# testFunc(2, c=5, d=6) 
# print()
# testFunc(10)
