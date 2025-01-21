#Accepts the students first name, last name, and ID number as arguments and returns the students login name as a string. 
def get_login_name(first, last, idnumber):
    #Getting the first three letters of the first name. 
    fname = first[0 : 3]

    #Getting the first three letters of the last name. 
    lname = last[0 : 3]

    #Getting the last three letters of the ID number. 
    id = idnumber[-3:]

    #Concatentating the three sets of characters to generate the username. 
    login_name = fname + lname + id

    #Return the login name
    return login_name

#Generating a password and verify it through length, uppercase, lowercase and digits. 
def verify_password(password): 
    #Setting values to false
    password_length = False
    password_uppercase = False
    password_lowercase = False
    password_digit = False
    
    #Testing to make sure password is at least 7 characters. 
    if len(password) >= 7: 
        password_length = True
        
        #Testing for at least 1 digit, uppercase letter and lower case letter. 
        for ch in password: 
            if ch.isupper(): 
                password_uppercase = True
            if ch.islower():
                password_lowercase = True
            if ch.isdigit():
                password_digit = True
    
    #If all requirements are met the password is set to true
    if password_length and password_uppercase and password_lowercase and password_digit:
        requirements_met = True
    else:
        requirements_met = False
    
    #Return the requirements_met variable
    return requirements_met
                
#Obtain the students first name, last name, and ID number then call function get_login_name to create string. 
#Gets password from user and validates it. 
def main(): 
    #Getting input from user
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your student ID number: ")

    print("Your system login name is: ")
    print(get_login_name(first, last, idnumber))
    
    #Getting input from user
    password = input("Enter your password: ")
    
    #validating the password
    while not verify_password(password):
        print("This password is not valid")
        password = input("Enter your password: ")
    
    print("That password is valid. ")

#Call main function
if __name__ == "__main__":
    main()


