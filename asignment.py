def shutdown(command):
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown Aborted."
    else:
        return "Sorry, I dont understand."
    
#example usage
user_input = input("Do you want to shut down? (yes/no): ")
print(shutdown(user_input))