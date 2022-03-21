# @TODO: Your code here
pet_info = {
    "name": "Rex",
    "age":3, 
    "Hobbies": ["eating", "sleeping"], 
    "wake-up":{"Monday": 4, "Friday": 8}
}
print(f'Hello my name is: {pet_info["name"]}')
print(f'Hobbies are: {pet_info["Hobbies"][0]}')
print (f'Wake up time: {pet_info["wake-up"]["Monday"]}')