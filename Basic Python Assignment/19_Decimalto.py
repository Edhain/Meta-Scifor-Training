# Function to convert decimal to binary
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Function to convert decimal to octal
def decimal_to_octal(n):
    return oct(n).replace("0o", "")

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

# Main program
if __name__ == "__main__":
    decimal_number = int(input("Enter a decimal number: "))
    
    binary_number = decimal_to_binary(decimal_number)
    octal_number = decimal_to_octal(decimal_number)
    hexadecimal_number = decimal_to_hexadecimal(decimal_number)
    
    print(f"Binary: {binary_number}")
    print(f"Octal: {octal_number}")
    print(f"Hexadecimal: {hexadecimal_number}")
