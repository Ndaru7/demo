# TODO APP

database = {1: ["todo list", "✓"],
            2: ["todo list 2", "X"]}

while(1):
    print("===TODO APP===")
    print("No | " + " "*15 + "Todo List" + " "*15 + " | Status")
    print("-"*60)
    for data in database.values():
         print(f"    {' '*15} {data[0]} {' '*15}  {data[1]}")

    print("-"*60 + "\n")
    print("1. add list")
    print("2. update list")
    print("3. delete list")
    print("4. exit app\n")

    user_input = input("[SELECT]> ")

    if user_input == "1":
        print("[INFO] add list\n")
        break

    elif user_input == "2":
        print("[INFO] update list\n")
        break

    elif user_input == "3":
        print("[INFO] delete list\n")
        break
    
    elif user_input == "4":
        print("[INFO] exit app\n")
        break

    else:
        print("[ERROR] Terjadi kesalahan\n")
