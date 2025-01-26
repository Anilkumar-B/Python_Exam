"""10. Bill Splitter
- Create a program to split a bill among a group of people:
- Input: Total bill amount, number of people, and any tip percentage.
- Output: Amount each person has to pay."""


def bill_splitter(total_bill_amount, number_of_people, tip_percentage):
    tip_amount = (total_bill_amount * tip_percentage) / 100
    total_amount_to_be_paid = total_bill_amount + tip_amount
    amount_per_person = total_amount_to_be_paid / number_of_people
    return amount_per_person

total_bill_amount = float(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

if total_bill_amount > 0 and number_of_people > 0 and tip_percentage >= 0:
    amount_per_person = bill_splitter(total_bill_amount, number_of_people, tip_percentage)
    print(f"Each person has to pay: Rs{amount_per_person:.2f}")
else:
    print("Invalid input. Please ensure all values are positive and valid.")

