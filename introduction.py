#print("hello python world")
#address = input("Enter address:")
#phone = input("Enter phone: ")
#country = input("Enter country: ")
#email = input("enter email: ")
#print(f"My name is : {} Address: {} Phone: {} Country: {} ". format( name,address,phone,country))

#data = [1234, 'ram' , True, 'python', 'java']
#print (type(data))

#access index
#print(data[0])
#print(data[1])
#print(data[4])


#data = [
    # [1,2,3,4,5,6],
    # [7,8,9,10,11,12,[[123,456,789,[67,88,666]]],
    # ]]
#print(data[1][6][0][3][2])

# data = {
#     "name": 'ram'
#     "address":'kathmandu'
# }
# print(data['name'])

users = {
    "name": "sophia",
    "address": {
        "province": {
            "p1": {
                "pname": "jhapa"
            }
        }
    },
    "contact": {
    "phone": "098768",
    "mobile": "98765"
    }
}

print(users['name'])
print(users['address']['province']['p1']['pname'])