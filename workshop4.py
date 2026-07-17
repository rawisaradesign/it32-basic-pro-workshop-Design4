gang_members = []
def  add_member(name,age,gang):
    new_member = {
        "name" : name,
        "age" : age,
        "gang" : gang
    }
    gang_members.append(new_member)
    return new_member
while True:
    choice = input("1 = add member : 2 = list member : 3 = quit : ")
    if choice == "1":
        input_name = input("name : ")
        input_age = int(input("age : "))
        input_gang = input("gang : ")
        add_member(input_name,input_age,input_gang)
        print("add member already")
    elif choice == "2":
        print("My Gang")
        print(gang_members)
    else :
        print("quit")
        break
