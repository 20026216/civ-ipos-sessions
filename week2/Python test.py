def modify_list(lst):
    lst.append("new")
    lst = ["completely", "new"]
    print(id(lst))

items = ["original"]
print(id(items))
modify_list(items)
print(items)