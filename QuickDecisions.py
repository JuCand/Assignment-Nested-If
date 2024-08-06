# Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))
venue = "Large hall" if attendees >= 100 else "Conference room"
print(venue) if attendees < 100 else print(venue , "also consider an audio system and projector.")





# Task 2: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

meal = input("Are you a Vegetarian, yes or no? ")
print("Veggie Delight Caterers") if meal == "yes" else print("Gourmet Meals Caterers")
