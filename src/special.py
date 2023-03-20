import gc

import micropython

gc.collect()
micropython.mem_info()
print("-----------------------------")
print("Initial free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
micropython.mem_info(True)


# noinspection PyUnusedLocal
def func():
    a = bytearray(50_000)
    b = bytearray(50_000)
    c = bytearray(50_000)
    d = bytearray(50_000)


print("-----------------------------")
print("Initial free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))

gc.collect()
print("Func definition: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
func()
print("Func run free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
gc.collect()
print("Garbage collect free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
print("-----------------------------")
micropython.mem_info(True)
