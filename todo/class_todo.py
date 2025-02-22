class Todo:

    database = {"0": ["name", "status"], "1": ["nama1", "status1"]}

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def checklist():
        print("==CHECKLIST==")

    def add_list():
        print("==ADD LIST==")

    def read_list():
        for key, value in Todo.database.items():
            print(f"{key.ljust(4)}| {value[0].ljust(57)}| {value[1].ljust(10)}")

    def update_list():
        pass

    def delete_list():
        pass

    def show_menu():
        print("\n===MENU===")
        print("1. Checklist")
        print("2. Add list")
        print("3. Update list")
        print("4. Delete list")
        print("5. Exit")

while True:
    print("[TODO APP]".center(70))
    print("="*75)
    print("ID".center(3), "|", "Name".center(56), "|", "Status".center(10))
    print("="*75)
    Todo.read_list()
    Todo.show_menu()
    usr_menu = input("\n[INPUT]: ")

    if usr_menu == "1":
        pass
    elif usr_menu == "2":
        pass
    elif usr_menu == "3":
        pass
    elif usr_menu == "4":
        pass
    elif usr_menu == "5":
        print("Exit program...")
        break
    else:
        print("Something wrong :(")