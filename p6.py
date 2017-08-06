#FIind out whether alist is a palindromo.
#判断一个列表是不是混问的。

def my_list_reverse(alist):
	clist = alist[:]
	blist = []
	for each in alist:
		blist.insert(0, each)
	if clist == blist[:]:
	   	print ("这个列表是回文。")
	else:
	   	print ("这个列表不清真。")
	return blist  #不return就是none，所以应该return点什么好呢。

#test
print(my_list_reverse([1,2,'a',2,1]))
print(my_list_reverse([1,2,'a',3,4]))

