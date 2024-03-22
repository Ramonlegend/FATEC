def register_user():
  users = []  # List to store user information
  
  name = input("Enter your name: ")
  age = input("Enter your age: ")
  email = input("Enter your email: ")
  
  user = {
    "name": name,
    "age": age,
    "email": email
  }
  
  users.append(user)  # Add the user to the list
  
  print("User registered successfully!")
  
register_user()