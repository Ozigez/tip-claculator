# This tip calculator returns the amount to be paid by each person when a bill is split.The code takes in the total bill in $,the number of people among whom the bill is to be shared, as well as the tip percentage.

print("Welcome to the tip calculator!")

bill= float(input("How much is the total bill:\n $"))
friends=int(input("Total number of peopele to share bill:\n"))
tip_percentage= float(input("percentage tip you want to give:\n"))/100

tip=bill * tip_percentage
total_bill =bill + tip
bill_per_person=round(total_bill/friends,2)
print(f"Each person is to pay ${bill_per_person}.")
  
