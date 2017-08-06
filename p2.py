#Find the last but one element of a list.
#写一个函数，使其接受一个列表，返回列表的倒数第二个元素。

def my_last(ky):
    return ky[-2]

#test
print(my_last([1,2,3,4,'qwe','asd','zxc','wer',5,6]))
print(my_last([1,2,3,4,'qwe','asd','zxc','wer']))
print(my_last([1,2,3,4,'qwe','asd','zxc']))
print(my_last([1,2,3,4,'qwe']))
print(my_last([1,2,3,4]))
