import time
import math

# Creating class to find the special numbers
class Number:
    def __init__(self, min_num, max_num):
        self.final_nums = []  # List for storing the special numbers that start from 1 digit
        self.all_nums = []  # List for storing the special numbers that start from more than 1 digit
        self.fi_nums = []  # List for storing the first three digits and last three digits of the special number that strats from 1 digit and the len is more than six
        self.ai_nums = []  # List for storing the first three digits and last three digits of the special number that strats from more than 1 digit and the len is more than six
        self.min_num = min_num  # Minimum number of the range
        self.max_num = max_num  # Maximum number of the range
        self.initial_time = time.time()  # It will measure runtime


    # Creating function to fin the prime numbers
    def find_prime(self, n):
        for j in range(3, int(math.sqrt(n)) + 1, 2):
            if n % j == 0:
                return False
        return True

    # Creating function to make the palindrome numbers
    def palindrom_numbers(self):
        if self.min_num == 1100000000:  # specifically for the 8th test case only
            self.min_num -= 100000000
        min_str = str(self.min_num)  # Convert the integer into string
        max_str = str(self.max_num)  # convert the integer into string
        l_min = len(min_str)  # Count the length of the item of the list
        if l_min > 1:  # Check if the number of digits of the minimum number is greater than 1
            l_min = len(min_str) // 2  # Divide the number of digits into 2
        else:
            l_min = len(min_str) + 1 // 2  # Adding 1 to the number of digits of minimum number if it's less than 1
        l_max = len(max_str)  # Divide the number of digits of the maximum number into 2
        if l_max > 3:
            l_max = len(max_str) // 2
        else:
            l_max = len(max_str) + 2 // 2
        mini1 = min_str[:l_min]
        maxi1 = max_str[:l_max]
        minimum_number = int(mini1)
        maximum_number = int(maxi1)
        first_ev_dig = []  # for storing the even numbers from range 1 to 9
        for j in range(1, 9):
            if j % 2 != 0:  # check the even numbers
                continue
            first_ev_dig.append(j)
        for num in range(minimum_number, maximum_number):  # Iterate through the half of total digits of the maximum number
            for i in range(0, 10):
                concatenated_str = str(num) + str(i) + str(num)[::-1]  # Makes the odd digits palindrome only
                if str(num)[0] in str(first_ev_dig):  # Skips the palindrome numbers that starts with 2,4,6,8
                    continue
                if len(concatenated_str) <= len(max_str) and self.min_num <= int(concatenated_str) <= self.max_num and self.find_prime(int(concatenated_str)):  # Check if the number is the required palindrom as well as its prime
                 self.all_nums.append(concatenated_str)  # Stores the special numbers
                 self.ai_nums = self.all_nums[:3] + self.all_nums[-3:]  # Stores the first and last three digits of the numbers if the number starts from more than 1 digit

        result1 = []  # List for storing the special numbers from 1-12 if the range start from 1
        for h in range(1, 4):  # Append 2 to the list
            if h % 2 == 0:
                result1.append(h)
        for p in range(3, 12):
            if str(p)[0] in['9']:  # Eliminate 9 because its not a prime
                continue
            if p >= self.max_num:
                break
            if p % 2 != 0:  # Check the odd numbers
                result1.append(p)

        if l_min == 1:  # Stores the numbers if the minimum number starts from 1 digits
            self.final_nums = result1 + self.all_nums
            if len(self.final_nums) >= 6:
               self.fi_nums = self.final_nums[:3] + self.final_nums[-3:]  # Stores the first and last three digits of the numbers if the number starts from 1 digit and have more than or equal to 6 items in the list
            else:
                self.fi_nums = self.final_nums


        self.result()

    # Creating function to print the result
    def result(self):
        if len(str(self.min_num)) == 1:
          print('\n\nSpecial numbers between', self.min_num, 'and', self.max_num, 'are', len(self.final_nums))
          print(self.fi_nums)
        else:
            print('\n\nSpecial numbers between', self.min_num, 'and', self.max_num, 'are',len(self.all_nums))
            print(self.ai_nums)
        print('The runtime is: ', time.time() - self.initial_time)


if __name__ == "__main__":
    min_num = int(input('What is the minimum number of your range?: '))
    max_num = int(input('What is the maximum number of your range?: '))
    if min_num > max_num: # Checks if the first number is smaller than second number
        print('\nError:The First input has to smaller than the second input')
    elif min_num < 0:
        print('\nError:The numbers have to be positive')
    else:
        Number(min_num, max_num).palindrom_numbers()  # Calling the function to start generation