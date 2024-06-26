try:
    # Open the file "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Hello, Lets explore file handling by doing 1, 2, 3.\n")
        file.write("what if we do a multiplication of some numbers here : 4*4\n")
        file.write("Its already night, Can we do this tomorrow .\n")

    print("We wrote into  'my_file.txt' and then we will read it later.")

    # Open the file "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        file_contents = file.read()

    # Display the contents of the file on the console
    print("Contents of 'my_file.txt':")
    print(file_contents)

    # Open the file "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write(" remembered something, we need to append.\n")
        file.write("Append this 0988676 and 67890\n")
        file.write("Lets call it a function to open.\n")

    print("Three additional lines appended to 'my_file.txt'.")

except FileNotFoundError:
    print("FileNotFoundError: The specified file does not exist.")
except PermissionError:
    print("PermissionError: Permission denied while trying to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # if no error
    print("Execution completed.")
