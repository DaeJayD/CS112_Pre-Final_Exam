import time

print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Dae Jay B. Doños")
time.sleep(1)
print("\nRULES TO CONSIDER:")
print("[1] If number (start) is a negative number, the program will prompt a message 'Enter a non-negative number.'")
print("[2] If number (end) is less than number (start), the program will prompt a message 'Enter a number greater than number (start).'")
print("[3] If the number is == '0', the program will terminate.")
time.sleep(0.5)

while True:
    start = int(input("\nEnter a number(start): "))

    while start < 0:
        print("Enter a non-negative number.")
        start = int(input("Enter a number(start): "))

    if start == 0:
        print("Program terminated.")
        break

    end = int(input("Enter a number(end): "))

    if end <= start:
        print("Enter a number greater than start.")
    else:
        print("\nPrime numbers between {} and {} are:".format(start, end))
        for num in range(start, end + 1):
            if num > 1:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(num, end=" ")
                    time.sleep(0.1)