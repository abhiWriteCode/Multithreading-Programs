def foo(bar, baz):
    print ('hello {0}'.format(bar))
    return 'foo' + baz

def boo(s):
    return "Sexy " + s

from multiprocessing.pool import ThreadPool

pool1 = ThreadPool(processes=1)
pool2 = ThreadPool(processes=1)

async_result = pool1.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process
return_val = async_result.get()  # get the return value from your function.
print(return_val)


async_result = pool2.apply_async(boo, ('Xev',)) # tuple of args for foo

# do some other stuff in the main process
return_val = async_result.get()  # get the return value from your function.
print(return_val)


sync_result = pool1.apply(foo, ('world', 'boo')) # tuple of args for foo

# do some other stuff in the main process
return_val = sync_result  # get the return value from your function.
print(return_val)