def fibonnaci(num):
    if num == 0 or num == 1:
        return num
    for i in cache:
        if i[0] == num:
            return i[1]
    
    value = fibonnaci(num-2) + fibonnaci(num-1)
    cache.append([num,value])
    return value
cache=[]
print(fibonnaci(400))