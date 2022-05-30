import re

def passchech(passwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compiling regex
    pat = re.compile(reg)
      
    # searching regex                 
    mat = re.search(pat, passwd)
      
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")
  
# Driver Code  
password = input("Enter your password: ")

if __name__ == '__main__':
    passchech(password)