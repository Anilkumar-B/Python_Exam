"""19. Find Second Largest Number
- Write a program to find the second largest number in a list provided by the user."""

def second_largest_num():
    arr = list(map(int, input("Enter numbers: ").split()))

    if len(arr) < 2:
        return "There is no second largest number."
    arr.sort(reverse=True)
    if arr[0] == arr[1]:
        return "There is no second largest number."
    else:
        return arr[1]
print(second_largest_num())
