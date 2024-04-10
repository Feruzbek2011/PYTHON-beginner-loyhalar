from time import sleep
import math
def delay(fn, ms, *args):
	sleep(ms / 1000)
	return fn(*args)
print("Birozdan so`ng kvadrat ildiz chiqarish:")
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))