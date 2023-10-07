print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
def Check_Vow(string, vowels):
    # The term "casefold" has been used to refer to a method of ignoring cases.
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)

    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1

    return count

# Driver Code
vowels = 'aeiou'
string = "Hi, I AM JOM BINOY AND I AM FROM KADUTHURUTHY"
print(Check_Vow(string, vowels))
