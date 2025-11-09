#my_dict={"python":"a type of snake"} #{key:value} , key value pair
#print(type(my_dict))

my_dict={"name":"Rose","age":19,"name":"Apsara"}
print(my_dict)

my_dictionary={
    "name":"Lily",
}
print(my_dictionary["name"]) #value accessing

my_dictionary["name"]="Jasmine"
print(my_dictionary)

#dictionary-  should be in curly bracket with key value pair
   #         - it is immutable
    #        - unique key


my_dictionary["City"]="KTM"
print(my_dictionary)

#removing: pop() del(), clear()
my_dict.pop("name")
print(my_dict)

del my_dict["age"]
print(my_dict)
my_dict.clear()
print(my_dict)
print("length of dict:" , +len(my_dict))

#methods = keys(), value(), items()
print(my_dictionary.keys())

print(my_dictionary.values())
# print(my_dictionary)

print(my_dictionary.items())
# print(my_dictionary)