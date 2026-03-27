def hanoi(n,source,auxillary,target,count=0):
    if n==1:
        print("move disk 1 from source",source,"to target",target)
        return 1
    
    count=hanoi(n-1,source,auxillary,target,count)
    print("move disk",n,"from source",source,"to target",target)
    count+=1
    count=hanoi(n-1,auxillary,target,source,count)
    return count

print(hanoi(3,'A','B','C'))
