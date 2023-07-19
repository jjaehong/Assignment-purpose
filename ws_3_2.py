number_of_people = 0
print(f"현재 가입 된 유저 수 : {number_of_people}")

def increase_user():
    pass

def create_user(name, age, address):
    user_info = dict()

    user_info["name"] = name
    user_info["age"] = age
    user_info["address"] = address
    print(f'{name}님 환영합니다!')

    increase_user()
    return user_info

print(create_user("홍길동", 30, "서울"))
import ws_3_1
print(ws_3_1.increase_user)

