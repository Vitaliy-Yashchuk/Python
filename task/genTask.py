# def func(start, end):
#     for x in range(start, end):
#         if(x%2!=0):
#             yield x

# for num in func(1,10):
#     print(num)
    
numbers = [1, 2, 5, 6, 7 , 8, 9 ,10]

def func2(list, start, end):
    for x in list:
        if(x<start or x>end):
            yield x
            
            
for num in func2(numbers,7,10):
    print(num)