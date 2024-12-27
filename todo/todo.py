# TODO APP

id = 0
database = {}

while(1):
    print("===TODO APP===")
    print("id | " + " "*15 + "Todo List" + " "*15 + " | Status")
    print("-"*60)
    for key,data in database.items():
         print(f"{key}    {' '*15} {data[0]} {' '*15}  {data[1]}")

    print("-"*60 + "\n")
    print("1. add list")
    print("2. update list")
    print("3. delete list")
    print("4. exit app\n")

    user_input = input("[SELECT]> ")

    if user_input == "1":
        print("[INFO] add list\n")
        input_id = id
        input_todo = input("Todo: ")
        input_status = "belum"

        database.update({input_id: [input_todo, input_status]})
        id += 1

    elif user_input == "2":
        print("[INFO] update list\n")
        print("[INFO] Masukan ID todo list yang ingin di Update")
        update_id = int(input("[INPUT] id: "))
        if update_id not in database:
            print("[ERROR] ID tidak ada pada database")
            break
        print("[INFO] Masukkan todo baru")
        update_todo = input("[INPUT] Todo: ")
        update_status = input("[INPUT] Status: ")
        database.update({update_id: [update_todo, update_status]})

    elif user_input == "3":
        print("[INFO] delete list\n")
    
    elif user_input == "4":
        print("[INFO] exit app\n")
        break

    else:
        print("[ERROR] Terjadi kesalahan\n")

    exit_option = input("[SELECT] Apakah sudah selesai? (y/n): ")
    if exit_option == "y" or exit_option == "y":
        break
