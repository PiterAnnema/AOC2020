import re

def checkHgt(val: str):
    hgt_match = re.search(r'^(\d{2,3})(cm|in)$', val)

    if not hgt_match:
        return False

    hgt_val, hgt_unit = hgt_match.groups()

    if hgt_unit == 'cm':
        if not 150 <= int(hgt_val) <= 193:
            return False
    elif hgt_unit == 'in':
        if not 59 <= int(hgt_val) <= 76:
            return False
    else:
        return False

    return True


tags = {
    'byr': lambda val: 1920 <= int(val) <= 2002, 
    'iyr': lambda val: 2010 <= int(val) <= 2020, 
    'eyr': lambda val: 2020 <= int(val) <= 2030, 
    'hgt': checkHgt, 
    'hcl': lambda val: re.match(r'^#([\da-f]*)$', val) is not None, 
    'ecl': lambda val: val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}, 
    'pid': lambda val: re.match(r'^(\d{9})$', val) is not None, 
    'cid': lambda _: True
}


def checkTags(passport: dict):
    missing = set(tags.keys()).difference(passport.keys())
    return not missing or missing == {'cid'}


def checkPassport(passport: dict):
    if not checkTags(passport):
        return False

    for tag, value in passport.items():
        if not tags[tag](value):
            return False

    return True


def getPassports(filename):
    pattern = re.compile(r'([a-z]{3}):(\S*)')
    passport = lambda data: {key: value for (key, value) in pattern.findall(data)}
    with open(filename) as f:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                yield passport(data)
                data = ''

        yield passport(data)


if __name__ == "__main__":
    passports = list(getPassports('data/day4.txt'))
    # Part 1
    print(sum(map(checkTags, passports)))

    # Part 2:
    print(sum(map(checkPassport, passports)))

