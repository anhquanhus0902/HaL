

def generate_random_octet_string(length):
    """
    Generate a random octet string of length bytes
    """
    import random
    return bytes([random.randint(0, 255) for _ in range(length)])

def octet_string_to_decimal(octet_string):
    """
    Convert an octet string to a decimal integer
    """
    return int.from_bytes(octet_string, 'big')

def decimal_to_octet_string(decimal):
    """
    Convert a decimal integer to an octet string
    """
    return decimal.to_bytes((decimal.bit_length() + 7) // 8, 'big')

a = generate_random_octet_string(10)
b = generate_random_octet_string(10)
print(a)
print(octet_string_to_decimal(a))
print(decimal_to_octet_string(octet_string_to_decimal(a)))