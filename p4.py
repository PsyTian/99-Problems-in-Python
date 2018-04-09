# Find the number of elements of a list.
# 计算一个列表一共有多少元素。

# 第一种
def my_list_length(ky):
    return len(ky)

# test
print(my_list_length([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))
print(my_list_length([1,2,3,4,'qwe',5,6,'sdf']))



# 第二种
def my_list_length(alist):
	k = 0
	for each in alist:
	    k = k + 1
	return k 

# test
print(my_list_length([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))
print(my_list_length([1,2,3,4,'qwe','asd','zxc','wer','sdf']))
