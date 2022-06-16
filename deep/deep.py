answer=input("What is the answer to...? ").strip().lower()

if answer == "42":
    output = "Yes"
elif answer == "fourty-two":
    output = "Yes"
elif answer == "fourty two":
    output = "Yes"
else:
    output = "No"
print (output)

