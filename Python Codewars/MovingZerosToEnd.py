# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
def move_zeros(array):
    zeroes = []
    values=[]
    for index,value in enumerate(array):
        if '0' in str(value) and value==0:
            print(index)
            zeroes.append(value)
        else:
            values.append(value)
            
    print(zeroes)
    for zero in zeroes:
        values.append(zero)
    print(values)
    return values
    