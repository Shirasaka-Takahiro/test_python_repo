class SimpleBulletinBoard:
    def __init__(self):
        self.messages = []
        self.post_count = 0
        self.users = {}

    def post_message(self, username, message):
        user_id = self.get_user_id(username)
        post_data = {"message_id": len(self.messages) +1, "user_id": user_id, "username": username, "message": message}
        self.messages.append(post_data)
        self.post_count += 1
        return post_data["message_id"]

    def get_user_id(self, username):
        if username not in self.users:
            self.users[username] = len(self.users) + 1
        return self.users[username]

    def get_messages(self):
        return self.messages
    
    def get_post_count(self):
        return self.post_count

    def search_messages(self, keyword):
        search_results = []
        for post_data in self.messages:
            if keyword.lower() in post_data["message"].lower():
                search_results.append(post_data)
        return search_results

    def delete_messages(self, message_id):
        for idx, post_data in enumerate(self.messages):
            if post_data["message_id"] == message_id:
                del self.messages[idx]
                self.post_count -= 1
                return True
        return False
    
    def edit_messages(self, message_id, new_message):
        for post_data in self.messages:
            if post_data["message_id"] == message_id:
                post_data["message"] = new_message
                return True
        return False


def main():
    bulletin_board = SimpleBulletinBoard()

    while True:
        print("1. Post a message")
        print("2. View messages")
        print("3. View post count")
        print("4. Search messages")
        print("5. Delete a message")
        print("6. Edit a message")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            message = input("Enter your message: ")
            message_id = bulletin_board.post_message(username, message)
            print(f"Message posted successfully! Message ID: {message_id}")
        elif choice == "2":
            messages = bulletin_board.get_messages()
            if messages:
                print("Messages:")
                for idx, post_data in enumerate(messages, 1):
                    message_id = post_data["message_id"]
                    user_id = post_data["user_id"]
                    username = post_data["username"]
                    message = post_data["message"]
                    print(f"{idx}. Message ID: {message_id}, User ID:{user_id}, {username}: {message}")
            else:
                print("No messages found.")
        elif choice == "3":
            post_count = bulletin_board.get_post_count()
            print(f"Total posts: {post_count}")
        elif choice == "4":
            keyword = input("Enter the keyword to search: ")
            search_results = bulletin_board.search_messages(keyword)
            if search_results:
                print("Search Results:")
                for idx, post_data in enumerate(search_results, start=1):
                    message_id = post_data["message_id"]
                    user_id = post_data["user_id"]
                    username = post_data["username"]
                    message = post_data["message"]
                    print(f"{idx}. Message ID: {message_id}, User ID:{user_id}, {username}: {message}")
            else:
                print("No matching messages found.")
        elif choice == "5":
            message_id_to_delete = int(input("Enter the Message ID to delete: "))
            if bulletin_board.delete_messages(message_id_to_delete):
                print(f"Message with ID {message_id_to_delete} deleted successfully.")
            else:
                print(f"Message with ID {message_id_to_delete} not found.")
        elif choice == "6":
            message_id_to_edit = int(input("Enter the Message ID to edit: "))
            new_message = input("Enter the new message: ")
            if bulletin_board.edit_messages(message_id_to_edit, new_message):
                print(f"Message with ID {message_id_to_edit} edited successfully.")
            else: 
                print(f"Message with ID {message_id_to_edit} not found.")
        elif choice == "7":
            print("Exiting the bulletin board.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
