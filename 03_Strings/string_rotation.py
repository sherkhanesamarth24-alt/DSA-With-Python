
# DSA - Strings Program 08: String Rotation

def is_rotation(str1, str2):

    if len(str1) != len(str2):
        return False

    combined = str1 + str1

    return str2 in combined


str1 = "ABCD"
str2 = "CDAB"

if is_rotation(str1, str2):
    print("Strings are Rotations")
else:
    print("Strings are Not Rotations")
