from DayTwo.Password import Password


def read_passwords():
    f = open("passwords.txt")
    passwords = f.read().splitlines()
    f.close()
    return passwords


def main():
    passwords = list(map(Password, read_passwords()))
    print("Part one: ", sum(x.validate_part_one() for x in passwords))
    print("Part two: ", sum(x.validate_part_two() for x in passwords))


if __name__ == "__main__":
    main()
