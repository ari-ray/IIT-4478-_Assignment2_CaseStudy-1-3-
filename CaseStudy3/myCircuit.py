#Name: Arittri Ray
#ID: u3312851
#Date: 12 September 2025
#CaseStudy3

def circuit_a(A: int, B: int, C: int) -> int:
    #Circuit_a

    #Converts integers to booleans
    A, B, C = bool(A), bool(B), bool(C)

    #Output: (AB’(A + C)) + ABC
    X = ((A and (not B)) and (A or C)) or (A and B and C)
    return int(X)


def circuit_b(A: int, B: int, C: int) -> int:
    #Circuit_b

    # Converts integers to booleans
    A, B, C = bool(A), bool(B), bool(C)

    # Output: AB’ + AC
    Y = (A and (not B)) or (A and C)
    return int(Y)




def main():
    print("~"*15 + "Boolean Circuit" + "~"*15)

    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))

    if A not in (0, 1) or B not in (0, 1) or C not in (0, 1):       #input validation
        print("Invalid input! Please enter only 0 or 1.")
        return

    # Run both circuits
    X = circuit_a(A, B, C)
    Y = circuit_b(A, B, C)

    print(f"Ouput of circuit_a: {X}")
    print(f"Ouput of circuit_b: {Y}")

    if X == Y:
        print("Both circuits are equivalent for this input.")
    else:
        print("Circuits are NOT equivalent for this input.")

if __name__ == "__main__":
    main()



