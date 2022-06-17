#input a large and small number
A = input("Enter in the larger number (A): ")
B = input("Enter in the smaller number (B): ")

larger = int(A)
smaller = int(B)

while smaller != 0:
  quotient = larger // smaller
  remainder = larger % smaller
  print("\nLet's divide", str(larger), "by", str(smaller), "and then find the remainder of the quotient")
  print("\nThe quotient of the two numbers is approx.", str(quotient), "and the remainder is", str(remainder))
  if remainder == 0:
    print("\nSince the remainder is 0, the program may stop")
    smaller = remainder
  else:
    print("\nThe smaller number will now become the larger number and the remainder will now become the smaller number")
    larger = smaller
    smaller = remainder

print("\nThe GCD of", A, "and", B, "is", larger)