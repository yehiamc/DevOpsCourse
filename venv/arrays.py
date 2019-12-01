my_list = ["pie", 3.14, True]
my_tuple= ("pie", 3.14, True)
my_dictionary = {300687162: {"name":"Yehiam", "age":32, "is a person":True}}

my_dictionary[300687162]["lastname"] = "Cohen"
my_dictionary[300687162]["name"] = "yehi"

# print(my_dictionary["name"])
# print(my_dictionary.keys())
# print(my_dictionary.values())


for key in my_dictionary.keys():
    print(key, "is", my_dictionary[key])
# my_list.append("is a list") #give the oprion to add to list
# my_list.append(True)

# for item in my_list:
#     print(item)
#
# for item in my_tuple:
#     print(item)
