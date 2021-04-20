mylist1=[12,-7,5,64,-14], mylist2=[12,14,-95,3]
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
#iterating each number in  list
for num in range(start,end + 1):
  #checking the condition 
  if num >= 0:
    print(num, end = " ")

#output list1 = 12,5,64
#output list2 = 12,14,3
