from typing import Counter


pets = [
    {"name" : "구름", "age":5},
    {"name" : "초코", "age":3},
    {"name" : "아지", "age":1},
    {"name" : "호랑이", "age":1}
]

print("# 우리 동네 애완 동물들")
# for i in range(len(pets)):
#     print(pets[i]['name'], str(pets[i]['age']) + '살')

# for pet in pets:
#     print(pet['name'], str(pet['age'])+'살')

# numbers = [1,2,3,3,5,4,2,6,5,7,1,9,8,5,2,4,5,6,7,9,7,8]
# cnt = {}

# for number in numbers:
#     if number in cnt:
#         cnt[number] += 1
#     else:
#         cnt[number] = 1
# print(cnt)

character = {
    "name":'기사',
    "level":12,
    "items": {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill": ["배기", "세게 배기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for item in character[key]:
            print(item, ":", character[key][item])
    elif type(character[key]) is list:
        for s in range(len(character[key])):
            print(key, ":", character[key][s])
    else:
        print(key, ":", character[key])
