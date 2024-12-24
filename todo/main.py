# TODO APP

database = {}

while(1):
    print("===TODO APP===")
    for data in database:
        print(data)

    print("1. add list")
    print("2. update list")
    print("3. delete list")
    print("4. exit app\n")

    user_input = input("[SELECT] ")

    if user_input == "1":
        print("[INFO] add list\n")
        break
    elif user_input == "2":
        print("[INFO] update list\n")
        break
    elif user_input == "1":
        print("[INFO] delete list\n")
        break
    elif user_input == "1":
        print("[INFO] exit app\n")
        break
    else:
        print("[ERROR] Terjadi kesalahan\n")
