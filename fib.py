import sys
sys.set_int_max_str_digits(10000000)

cache=[]
def fibonnaci(num):
    if num == 0 or num == 1:
        return num
    for i in cache:
        if i[0] == num:
            return i[1]
    
    value = fibonnaci(num-2) + fibonnaci(num-1)
    cache.append([num,value])
    return value
def test_normal_fibonnaci():

    print(fibonnaci(40000))

def dp_fib(num):
    if len(cache)<1:
        cache.append(0)
    if len(cache)<2:
        cache.append(1)
    if num<=0:
        return 0
    for i in range(len(cache), num+1):
        cache.append(cache[i-1] + cache[i-2])

    return cache[num]
print(dp_fib(40000))
cache=[]
test_normal_fibonnaci()