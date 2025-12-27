# it is data format for comunication between front end and back end.
# it is always use for data exchange.
# JSON----java script object notation
# it is very lightweight data format.
# easy to read and write
# it is language independent
# based on java script syntax
# it is use for API communication like REST , Graphql.
# it is also use for configuration file , in data storage and in web and mobile app
# data is stored in the format of key - value pair.
# keys are always in string using double quotes.
# we can use nested objects in json.
# values can be int , bool ,array , string object,null.
# use "json lint" website to validate your json.




# Basic structure example:---------
# {
#     "name":"pranav",
#     "age":21,
#     "isStudent":False,
#     "skills":["python","C","C++","java"],
#     "address":{
#         "street":"1/23",
#         "city":"delhi",
#         "pincode":110234
#     },
#     "test":null
# }




# rules for json:-----
# 1.keys must be in double quotes.
# 2.string must be in double quotes.
# 3.no comments are allowed.
# 4.no tralling commas





# nested objects in json:------


# {
#     "users":[
#         {"name":"pranav","age":24},
#         {"name":"harsh","age":23}
#     ]
# }




# json in python:------->


# json_user="""
# {
#     "name":"pranav",
#     "phone":"7050040030",
#     "skills":["java","python","c++","c"],
#     "address":{
#         "city":"saharsa",
#         "pincode":852124
#     }
# }
# """
# print(json_user)
# print(type(json_user))




# use json in an object:------


# import json
# json_user= """
# {
#     "name":"pranav",
#     "phone":"7050040030",
#     "skills":["java","python","c++","c"],
#     "address":{
#         "city":"saharsa",
#         "pincode":852124
#     }
# }
# """
# userDict=json.loads(json_user)
# print(userDict)
# print(type(userDict))
# print(userDict['name'])
# print(userDict['phone'])





# convert dictonary into json:-----

# import json
# todo={"title":"python","isComplete":False}
# json_todo=json.dumps(todo)
# print(json_todo)