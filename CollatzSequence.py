"""The Collatz sequence is a sequence of numbers relevant to the Collatz conjecture,
 which theorizes that any number using this algorithm will eventually be reduced to 1.
 The conjecture's truth is supported by calculations, but it hasn't yet been proved that no number can indefinitely stay above 1."""

print("This is Collatz Sequence")

number=int((input("Enter a number: ")))

def collatzsequence(number):
    print("collatzsequence: ", number, end="")


while number != 1:
    if number % 2 == 0:
        number = number // 2
        print("→", number, end="")

    else:
        number = 3 * number + 1
        print("→", number, end="")

    if number == 1:
        break
    print(int(number), end="")

