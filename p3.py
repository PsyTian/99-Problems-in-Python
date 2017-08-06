#Find the K'th element of a list.
#写一个函数，使其接受一个列表和序号K,返回列别的第K个元素。

def function(list,k):
    return list[k-1]

#test    
print(function([1,2,3,4,'qwe','asd','zxc','wer',5,6],5))
print(function([1,2,3,4,'qwe','asd','zxc','wer',5,6],6))
print(function([1,2,3,4,'qwe','asd','zxc','wer',5,6],9))