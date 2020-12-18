from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Union


class Passport(NamedTuple):
    byr: int  # (Birth Year)
    iyr: int  # (Issue Year)
    eyr: int  # (Expiration Year)
    hgt: str  # (Height)
    hcl: str  # (Hair Color)
    ecl: str  # (Eye Color)
    pid: int  # (Passport ID)
    # cid: int # (Country ID)


def check_passport(passport: Dict[str, str]) -> bool:
    for field, val in passport.items():
        temp_pass: Dict[str, Union[str, int]] = {}
        newval: Union[int, str]
        if field in ['byr', 'iyr', 'eyr', 'pid']:
            try:
                newval = int(val)
            except Exception as ex:
                print(f'invalid passport: {ex}')
                return False
        else:
            newval = val
        temp_pass[field] = newval
    try:
        x = Passport(**temp_pass)  # type: ignore # noqa
    except Exception as ex:
        print(f'invalid passport: {ex}')
        return False
    return True


def num_valid(passports: List[Dict[str, str]]) -> int:
    valid = 0
    for p_dict in passports:
        p_dict.pop('cid', None)
        valid += check_passport(p_dict)
    return valid


if __name__ == "__main__":

    passports: List[Dict[str, str]] = []
    with open('input') as file:
        p_dict: Dict[str, str] = {}
        for line in file.readlines() + [""]:
            # print(type(line),p_dict)
            if line.strip():
                for pair in line.split():
                    key, value = pair.split(':')
                    p_dict[key] = value
            else:
                passports.append(p_dict)
                p_dict = {}
    print(num_valid(passports))
