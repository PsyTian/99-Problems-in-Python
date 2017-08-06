def my_last(ky):
    return ky[-1]
print(my_last([1,2,3,4,'qwe','asd','zxc','wer',5,6]))

my_last = [1,2,3,4,'qwe','asd','zxc','wer',5,6,'ddf']
for each in my_last:
	print(each)


def my_last(ky):
    return len(ky)
print(my_last([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))

  #print(reverse([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))




#def reverse(l):
#	blist = list(l)
#	return blist.reverse() or blist
reverse = [1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']
blist = [1,2,3,4]
if blist == reverse:
	print("这列表是回文。")
else:
	print("这列表不清真。")

# Python style. WHY? See "Boolean logic in Python"
def palindrome_p(alist):
    return cmp(alist, my_reverse(alist))
    
# Clearer to users    
def palindrome_another(alist):
    if cmp(alist, my_reverse(alist)) == 0:
        print ("The list is palindrome")
    else:
        print ("The list is not palindrome")

#test
print(palindrome_p([1,2,3,4,4,3,2,1]))




#p7
def flatten_list(input_list):
    output_list = []
    while True:
        if input_list == []:
            break
        for index, i in enumerate(input_list):

            if type(i)== list:
                input_list = i + input_list[index+1:]
                break
            else:
                output_list.append(i)
                input_list.pop(index)
                break
    return output_list

#test
print(flatten_list([1,2,3,4,['qwe','asd','zxc','wer',[5,6],'sdf']]))
print(flatten_list([1,2,3,4,'qwe','asd','zxc','wer',5,6,'sdf']))    