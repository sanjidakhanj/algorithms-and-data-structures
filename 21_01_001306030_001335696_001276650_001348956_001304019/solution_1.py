import time


# Creating Class SpecialNumbers
class SpecialNumbers:
    def __init__(self, start_number, end_number):
        self.special_numbers = []  # List for storing special numbers
        self.start_number = start_number  # Starting range
        self.end_number = end_number  # Ending range
        self.starting_time = time.time()  # Starting time

    # Function to check prime number
    def is_prime(self, number):
        if number <= 1:  # Check if the number is less than or equal 1
            return False
        elif number == 2:  # Check if the number is equal 2
            return True
        elif number % 2 == 0:  # Check if the number is divisible by 2
            return False

        # Check for divisors from 3 to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):  # Optimized by group changing step from 4 to 2
            if number % i == 0:  # Optimized by group removed one if statement
                return False  # Number is divisible, not prime
        return True  # Number is prime

    # Function to generate palindromes with an algorithm
    def generate_palindromes(self):
        number_str = str(self.start_number)  # Converting starting number to string
        number_half_len = (len(number_str) // 2) - 1  # Getting half of length of digits in the number and subtracts 1

        # Making sure that number_half_len is not less than 0
        if number_half_len <= 0:
            number_half_len = 1

        number_to_double = number_str[:number_half_len]  # Determining the number of digits need to be used

        # Changing the number of digits to if the merging is less than starting number
        while int(number_to_double + number_to_double[::-1]) <= self.start_number:
            number_half_len += 1
            number_to_double = number_str[:number_half_len]

        # Subtracting 1 from number_half_len if it's greater than 1
        if number_half_len > 1:
            number_half_len -= 1
            number_to_double = number_str[:number_half_len]
        elif number_half_len == 1:  # If the starting number is single digit then it checks from number 1
            number_to_double = 1

        # for loop runs from the number that can be double/merge to obtain a palindrome
        for a in range(int(number_to_double), self.end_number+1):
            new = str(a)  # Converting iterated number to string
            even_len_palindrome = int(new + new[::-1])  # Generating palindrome model of even length of digits
            odd_len_palindrome = int(new + new[-2::-1])  # Generating palindrome model of odd length of digits

            # Checking if the palindrome is in the required range and is it a prime number
            if self.start_number <= even_len_palindrome <= self.end_number and self.is_prime(even_len_palindrome):
                self.special_numbers.append(even_len_palindrome)
            if self.start_number <= odd_len_palindrome <= self.end_number and self.is_prime(odd_len_palindrome):
                self.special_numbers.append(odd_len_palindrome)

            # Breaking the for loop if the palindrome is out of the required range
            if odd_len_palindrome > self.end_number and odd_len_palindrome > self.end_number:
                break
        self.print_result()  # Calling function to print the output

    # Function to obtain the three smallest & largest special numbers in the range if total no. special numbers exceed 6
    def min_max(self, lst):
        sorted_list = sorted(lst)  # Sorting the special numbers list
        if len(sorted_list) > 6:  # Checking if the total number of special numbers is greater than 6
            sorted_list = sorted_list[:3] + sorted_list[-3:]
        return sorted_list

    # Function to print the final output of the program
    def print_result(self):
        print('\n\nThere are', len(self.special_numbers), 'special numbers between', self.start_number, 'and', self.end_number)
        print('Special numbers are ', self.min_max(self.special_numbers))
        print('Time taken: ', time.time() - self.starting_time)  # Displays the time taken to find special numbers


if __name__ == "__main__":
    start_number = int(input('Enter the First number: '))
    end_number = int(input('Enter the Second number: '))
    if start_number >= end_number:  # Checks if the first number is smaller than second number or negative value
        print('\nError:The First number is needs to be smaller than second number')
    elif start_number < 0 or end_number < 0:
        print('\nError:The input needs to be positive integer')
    else:
        SpecialNumbers(start_number, end_number).generate_palindromes()  # Calling the function to start generation
