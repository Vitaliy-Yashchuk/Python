a = 10
b = 3

print(a / b)
print(a // b)

print(2 ** 8)

nickname = input("Enter you nickname:")

##### ------- types: int string float bool 
# int() float() str() 
age = int(input("Enter your age:"))

print(f"Nickname type: {type(nickname)}")
print(f"Age type: {type(age)}")

if age > 18:
    print("Allow")
else:
    print("Deny")

while not input("Enter 'A': ") == 'A':
    print("Try again!")

print("Have a good day!")

def checkPassword(password) -> bool:
    return len(password) >= 6 and '.' in password

print(checkPassword("Qwer"))
print(checkPassword("Qwer.3434"))