def birxil():
    a=1,3,4,5,6,8
    b=1,3,4,5,5,6,8
    x=0
    ab=[a,b]
    for a1 in ab:
        for value in a1:
            if a1.count(value)>1:
                x+=1
        if x>0:
            print(False)
        else:
            print(True)
birxil()

# # yoki

# def test_unikal(ruyxat):
#     if len(ruyxat) == len(set(ruyxat)):
#         return True
#     else:
#         return False;
# print(test_unikal([1,5,7,9]))
# print(test_unikal([2,4,5,5,7,9]))
