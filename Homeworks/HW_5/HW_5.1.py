div_2 = [x for x in range(1,10)if x % 2 == 0]
print(f"Even numbers divisible by 2 {div_2}.")

div_3 = [x for x in range(1,10)if x % 3 == 0]
print(f"Odd numbers divisible by 3 {div_3}.")

not_div_2_3 = [x for x in range(1,10)if x % 2 != 0 and x % 3 != 0]
print(f"Numbers not divisible by 2 or 3 {not_div_2_3}.")
