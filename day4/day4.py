#!/usr/bin/env python
# coding: utf-8


passports = []
with open('input', 'r') as file:
    p_dict = {}
    for line in file.readlines() + [""]:
        #print(type(line),p_dict)
        if line.strip():
            for pair in line.split():
                key, value = pair.split(':')
                p_dict[key] = value
        else:
            passports.append(p_dict)
            p_dict = {}


from typing import NamedTuple


class Passport(NamedTuple):
    byr: int # (Birth Year)
    iyr: int # (Issue Year)
    eyr: int # (Expiration Year)
    hgt: str # (Height)
    hcl: str # (Hair Color)
    ecl: str # (Eye Color)
    pid: int # (Passport ID)
    #cid: int # (Country ID)



pass_dict = {'ecl': 'brn',
             'pid': 9337568136,
             'eyr': 2026,
             'hcl': '#6b5442',
             'hgt': '69cm',
             #'iyr' :2019,
             'byr': 2025}
    
valid = 0
for p_dict in passports:
    p_dict.pop('cid', None)

    try:
        Passport(**p_dict)
        valid += 1
    except Exception as e:
        print(e)
        #print('bad passport!')
        #raise err





