value = input("Enter a four-digit natural number")
multiply = int(value[0])*int(value[1])*int(value[2])*int(value[3])
reverse = int(str(value)[::-1]) 
sort = sorted(value)

print("multiply=",multiply)
print("reverse=",reverse)
print("sort=",sort)