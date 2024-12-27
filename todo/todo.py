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

    print("[INFO] Pilih menu berdasarkan angka")
    user_input = input("[INPUT] ")

    # Bagian Add todo list
    if user_input == "1":
        print("[INFO] ADD LIST")
        input_id = id
        print("[INFO] Masukan todo list")
        input_todo = input("[INPUT] ")
        input_status = "belum"

        database.update({input_id: [input_todo, input_status]})
        id += 1
    
    # Bagian Update todo list
    elif user_input == "2":
        print("[INFO] UPDATE LIST")
        print("[INFO] Masukan ID todo list yang ingin di Update")
        update_id = int(input("[INPUT] "))
        if update_id not in database:
            print("[ERROR] ID tidak ada didatabase")
            continue

        print("[INFO] Masukkan todo baru")
        update_todo = input("[INPUT] ")
        print("[INFO] Masukan status baru")
        update_status = input("[INPUT] ")
        database.update({update_id: [update_todo, update_status]})

    # Bagian Delete todo list
    elif user_input == "3":
        print("[INFO] DELETE LIST")
        print("[INFO] Masukan ID todo list yang ingin di Delete")
        delete_id = int(input("[INPUT] "))
        if delete_id not in database:
            print("[ERROR] ID tidak ada didatabase")
            continue

        database.pop(delete_id)
    
    # Bagian exit program
    elif user_input == "4":
        print("[INFO] exit app\n")
        break

    else:
        print("[ERROR] Terjadi kesalahan\n") 
