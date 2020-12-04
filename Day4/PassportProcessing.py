import re
from Day4.Passport import Passport

f = open("passport_records.txt", "r")
records = re.split("\n\n", f.read())
f.close()

print("Valid Passports:", sum(map(lambda x: Passport(x).validate(), records)))
