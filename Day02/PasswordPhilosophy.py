from Day02.Password import Password


def read_passwords():
    f = open("passwords.txt", "r")
    password_records = f.read().splitlines()
    f.close()
    return list(map(Password, password_records))


passwords = read_passwords()
print("Part one: ", sum(x.validate_part_one() for x in passwords))
print("Part two: ", sum(x.validate_part_two() for x in passwords))
