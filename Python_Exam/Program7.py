"""7. Bank Loan Eligibility
- Develop a program to check loan eligibility:
- Input: Salary, age, and credit score.
- Output: Loan approval or rejection with reasons."""



def check_loan_eligibility(salary, age, credit_score):
    if age < 18:
        print("Loan Rejected: Age must be 18 or older.")
    elif salary < 25000:
        print("Loan Rejected: Minimum salary requirement is Rs.25,000.")
    elif credit_score < 700:
        print("Loan Rejected: Credit score must be 700 or higher.")
    else:
        print("Loan Approved: You meet all the eligibility criteria!")

def main():
    salary = input("Enter your monthly salary Rs: ")
    age = input("Enter your age: ")
    credit_score = input("Enter your credit score: ")

    if salary.replace('.', '', 1).isdigit() and age.isdigit() and credit_score.isdigit():
        salary = float(salary)
        age = int(age)
        credit_score = int(credit_score)

        if salary > 0 and age > 0 and credit_score >= 0:
            check_loan_eligibility(salary, age, credit_score)
        else:
            print("Invalid input: Please enter positive values for salary, age, and credit score.")
    else:
        print("Invalid input: Please enter numeric values for salary, age, and credit score.")

main()
