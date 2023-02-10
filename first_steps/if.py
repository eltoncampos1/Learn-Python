is_male = True
is_tall= True

if is_male and is_tall:
    print("You are male and Tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("you are not a male and not tall")