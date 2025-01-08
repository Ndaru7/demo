# TODO APP

"""
id = 0
database = {}

while(1):
    print("===TODO APP===")
    print("id | " + " "*15 + "Todo List" + " "*15 + " | Status")
    print("-"*60)
    for key,data in database.items():
         print(f"{key}    {' '*15} {data[0]} {' '*15}  {data[1]}")

    print("-"*60 + "\n")
    print("1. checklist")
    print("2. add list")
    print("3. update list")
    print("4. delete list")
    print("5. exit app\n")

    print("[INFO] Pilih menu berdasarkan angka")
    user_input = input("[INPUT] ")
    
    # Bagian Checklist todo
    if user_input == "1":
        print("[INFO] CHECKLIST")
        print("[INFO] Masukan ID todo yang ingin di checklist")
        checklist_id = int(input("[INPUT] "))
        if checklist_id not in database:
            print("[ERROR] ID tidak ada didatabase")
            continue

        checklist_todo = database[checklist_id][0]
        checklist_status = "selesai"
        database.update({checklist_id: [checklist_todo, checklist_status]})

    # Bagian Add todo list
    elif user_input == "2":
        print("[INFO] ADD LIST")
        input_id = id
        print("[INFO] Masukan todo list")
        input_todo = input("[INPUT] ")
        input_status = "belum"
        database.update({input_id: [input_todo, input_status]})
        id += 1
    
    # Bagian Update todo list
    elif user_input == "3":
        print("[INFO] UPDATE LIST")
        print("[INFO] Masukan ID todo list yang ingin di Update")
        update_id = int(input("[INPUT] "))
        if update_id not in database:
            print("[ERROR] ID tidak ada didatabase")
            continue

        print("[INFO] Masukkan todo baru")
        update_todo = input("[INPUT] ")
        update_status = database[update_id][1]
        database.update({update_id: [update_todo, update_status]})

    # Bagian Delete todo list
    elif user_input == "4":
        print("[INFO] DELETE LIST")
        print("[INFO] Masukan ID todo list yang ingin di Delete")
        delete_id = int(input("[INPUT] "))
        if delete_id not in database:
            print("[ERROR] ID tidak ada didatabase")
            continue

        database.pop(delete_id)
    
    # Bagian exit program
    elif user_input == "5":
        print("[INFO] exit app\n")
        break

    else:
        print("[ERROR] Pilihan tidak valid\n")

    test
"""
id = 0
database = {}

def check_todo():
    pass

def read_todo():
    print("===TODO APP===")
    print("id | " + " "*15 + "Todo List" + " "*15 + " | Status")
    print("-"*60)
    for key,data in database.items():
         print(f"{key}    {' '*15} {data[0]} {' '*15}  {data[1]}")

    print("-"*60 + "\n")
    print("1. checklist")
    print("2. add list")
    print("3. update list")
    print("4. delete list")
    print("5. exit app\n")

def create_todo():
    pass

def update_todo():
    pass

def delete_todo():
    pass

def main():
    while(1):
        read_todo()

        print("[INFO] Pilih menu berdasarkan angka")
        user_input = input("[INPUT] ")

        if user_input == "1":
            pass

        elif user_input == "2":
            pass

        elif user_input == "3":
            pass

        elif user_input == "4":
            pass

        elif user_input == "5":
            return "[INFO] Exit App"
            break
                    
        else:
            print("[ERROR] Pilihan tidak valid")

if __name__ == "__main__":
    print(main())

