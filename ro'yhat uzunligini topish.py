def test(strs):
	return [*map(len, strs)]
strs = ['mushuk', 'mashina', 'yaqin', 'markaz']
print("Original satr:")
print(strs)
print("Bo'sh bo'lmagan satrlar ro'yxatining uzunligi:")
print(test(strs))
strs = ['mushuk', 'it', 'xona', 'shirinlik', '', 'yedi', '']
print("\nOriginal satr:")
print(strs)
print("Bo'sh bo'lmagan satrlar ro'yxatining uzunligi:")
print(test(strs))