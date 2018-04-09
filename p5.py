# Reverse a list.
# 翻转一个列表里所有元素的顺序。

#第一种
def my_list_reverse(alist):
    blist = []
    for each in alist:
        blist.insert(0, each)   #list.insert 在某一特定位置前面添加一个数据项。
    return blist

# test
print(my_list_reverse([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))	
print(my_list_reverse([1,2,3,4,5,6]))
print(my_list_reverse(['qwe','asd','zxc','wer','sdf']))

# 第二种
def my_list_reverse(alist):
	blist = list(alist)
	return blist.reverse() or blist

# test
print(my_list_reverse([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))	
print(my_list_reverse([1,2,3,4,5,6]))
print(my_list_reverse(['qwe','asd','zxc','wer','sdf']))


