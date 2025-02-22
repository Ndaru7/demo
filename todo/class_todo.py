class Todo:

    database = {}

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def checklist():
        pass

    def add_list():
        pass

    def read_list():
        pass

    def update_list():
        pass

    def delete_list():
        pass

    def show_menu():
        print("===TODO APP===")
        print("1. Checklist")
        print("2. Add list")
        print("3. Update list")
        print("4. Delete list")
        print("5. Exit")

while True:
    todo = Todo.show_menu()
    usr_menu = input("[INPUT]: ")

    if usr_menu == "1":
        pass
    elif usr_menu == "2":
        pass
    elif usr_menu == "3":
        pass
    elif usr_menu == "4":
        pass
    elif usr_menu == "5":
        pass
    else:
        print("Something wrong :(")