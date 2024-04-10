if __name__=='__main__':
    n=int(input())
if n>=2 and n<=10:
    arr=map(int,input().split())
    new_set=sorted(set(arr))
    print(new_set[-2])
else:
    print("[2,10] oralig`idagi son kiriting")
