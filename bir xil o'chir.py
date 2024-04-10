from collections import OrderedDict
def a(str1):
	return "".join(OrderedDict.fromkeys(str1))
print(a("python dasturlash tili"))
print(a("amaliyot darsi"))