# VARIABLES
age1 = 18
age2 = 20
name = "Eren"
print("Your age is:",age1) 
print("Your age is now : " + str(age2))  #Type casting

print(type(age1),"\n",type(name))  #Checking the type 

# List Comprehension
double1 = []
for i in range(1, 11):
    double1.append(i * 2)

double2 = [i*2 for i in range(1, 11)]

print(double1)
print(double2)

nums = [-32, -13, 65, -6, -1, -8, 35, 89, 43, -24]
positive_nums = [i for i in nums if i >= 0]
negative_nums = [i for i in nums if i < 0]
print(positive_nums)
print(negative_nums)

lowercase_list = ["one", "two", "three", "four", "five"]
uppercase_list = [st.upper() for st in lowercase_list]
print(uppercase_list)