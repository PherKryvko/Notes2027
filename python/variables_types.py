#predict 
x = 10
y = x
x += 5
print(x, y)

a = [1]
b = a
a += [2]
print(a, b)


#question 2
age = int(input("Age: ")) + 1
print(age)


#4. Predict which of these succeed and which raise `ValueError`: 
    
int("42") #42
int(" 42 ") #42 ignores whitespace
int("4.2") #Val error 
float("4.2") #4.2
int("forty") #Val error
int("") #Val error

bool("False") #True as has a value
bool("") #False
bool(" ") #True as value
bool(0.0) #False
bool([]) #False
bool(None) #False
int(3.7) #3