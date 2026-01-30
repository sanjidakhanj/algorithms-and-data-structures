from solution_1 import SpecialNumbers

if __name__ == "__main__":
    SpecialNumbers(1, 2_000).generate_palindromes()
    SpecialNumbers(100, 10_000).generate_palindromes()
    SpecialNumbers(20_000, 80_000).generate_palindromes()
    SpecialNumbers(100_000, 2_000_000).generate_palindromes()
    SpecialNumbers(2_000_000, 9_000_000).generate_palindromes()
    SpecialNumbers(10_000_000, 100_000_000).generate_palindromes()
    SpecialNumbers(100_000_000, 400_000_000).generate_palindromes()
    SpecialNumbers(1_100_000_000, 15_000_000_000).generate_palindromes()
    SpecialNumbers(15_000_000_000, 100_000_000_000).generate_palindromes()
    SpecialNumbers(1, 1_000_000_000_000).generate_palindromes()
