number_of_people = 0
user_list = []

def increase_user():
     global number_of_people
     number_of_people += 1

def create_user(name, age, address):
    # user_info = dict()
    user_info = {}

    user_info["name"] = name
    user_info["age"] = age
    user_info["address"] = address

    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


for i in range(5):
     new_user = create_user(name[i], age[i], address[i])
     user_list.append(new_user)
     increase_user()


# for name, age, address in zip(name, age, address):
#      new user = create_user(name, age, address)
#      user_list.append(new_user)
#      increase_user()

print(user_list)

