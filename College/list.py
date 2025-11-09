#data structures: -list: ordered, mutable, diff datatypes
                #-tuple
                #-dict
                 #-set

my_list=[1,2,3,4]
print(type(my_list))
sub_list=my_list[3:0:-1]
print(sub_list)

#for loop
for i in my_list:
    print(i)

  #mutable = whether we can chnge the values in list
my_list[0]=10
print(my_list)

#string isn't mutable
#name = "Ram"
#name[0] = "S"
#print(name)

#functions
my_list.append("Sam")
print(my_list)

my_list.insert(2,"Lina")
print(my_list)

my_list.pop(2) #if no index is given, it pops the last element
print(my_list)

my_list.remove(2)
print(my_list)

print(len(my_list))

fruits=["apple","banana","canberry"]
#for loop
for i in range(len(fruits)): #range(3)
     print(i+1,fruits[i])
#while loop
i=0
while i<len(fruits):
    print(i+1,fruits[i])
    i+=1
    
#nested list - list within a list
#student = [["Lina","Gina"][22,21]]
#print(student)

#enumerate: 
for index, value in enumerate(fruits,start=15):
    print(index,value)

list_1=["a","b"]
list_2=["c","d"]
list_3=list_1+list_2
print(list_3)