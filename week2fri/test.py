p = {"num" : 1, "name": "Bob", "listofnum": [1, 2]}
print(p["num"])
print(p["name"])
print(p["listofnum"])
print(p["listofnum"][0])
i = input("num/name/listofnum")
print("user choose", i, p[i])
l = {4, 3, 1}
print(*l)