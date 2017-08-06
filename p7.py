#Flatten a nested list structure.
#对于一个复合列表（即：列表的列表）把它变成一个简单的列表。即，列表中含有原列表中的所有单个元素。

def flatten_list(alist):


#test
print(flatten_list([1,2,3,4,['qwe','asd','zxc','wer',[5,6],'sdf']]))
print(flatten_list([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))