# 6. Suppose, we have given list:
# a = [
# {“username”: “ram@gmail.com”, “last_login”: “157950”},
# {“username”: “ shyam @gmail.com”, “last_login”: “157659”},
# {“username”: “hari@gmail.com”, “last_login”: “157680”},
# {“username”: “krishna@gmail.com”, “last_login”: “157880”}
# ]
# # Sort the above given list according to their last_login in ascending order


a = [
{"username": "ram@gmail.com", "last_login": "157950"},
{"username": "shyam@gmail.com", "last_login": "152650"},
{"username": "hari@gmail.com", "last_login": "155750"},
{"username": "krishna@gmail.com", "last_login": "154950"},
]

a.sort(key=lambda x:x.get("last_login"))
print(a, end='')