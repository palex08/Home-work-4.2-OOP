class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Getter for user_id
    def get_user_id(self):
        return self._user_id

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for access_level
    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    # Method to add a user
    def add_user(self, user):
        self._user_list.append(user)

    # Method to remove a user by ID
    def remove_user(self, user_id):
        self._user_list = [user for user in self._user_list if user.get_user_id() != user_id]

    # Method to get the list of users
    def get_user_list(self):
        return self._user_list


# Example usage:
if __name__ == "__main__":
    # Create an admin
    admin = Admin(1, "Admin Gora")

    # Create some users
    user1 = User(2, "Sasha")
    user2 = User(3, "Petya")
    user3 = User(4, "Vasya")

    # Admin adds users to the system
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)



    # Display the list of users
    for user in admin.get_user_list():
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

    # Admin removes a user
    admin.remove_user(2)

    # Display the updated list of users
    for user in admin.get_user_list():
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
