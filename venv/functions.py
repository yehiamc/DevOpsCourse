# def my_func():
#     print("inside of function")
#
# def my_func2(number):
#     print(number, "from function")
#
# def my_func3(numa, numb):
#     return numa + numb
#
# my_func()
# my_func2(6)
# sum = my_func3(5, 10)
# print(sum)
#
# my_list = ["Yehiam", "Cohen", "Dana", "Kiani"]
#
#
# def my_function(my_list):
#     print(len(my_list))
#
#
# my_function(my_list)


def dict_validator(a_dict):

    if not type(a_dict["name"]) is str:
        print("name isn't string")
    if not type(a_dict["age"]) is int:
        print("age isn't number")
    if not type(a_dict["hobbies"]) is list:
        print("Hobbies isn't string")


my_dict = {"name": "Yehiam", "age": 32, "Hobbies": ["footaball", "movies"]}

dict_validator(my_dict)