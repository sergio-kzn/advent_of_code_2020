"""
"""
import re
import requests
import data


def get(url):
    headers = {
        'cookie': data.COOKIE}
    req = requests.get(url=url, headers=headers)

    return req.text


def check_year(data: int, min: int, max: int):
    if min <= data <= max:
        return True
    return False


def check_height(hgt: str):
    height = int(re.search('\d+', hgt).group(0))
    units_cm = re.search(r'cm', hgt)
    units_in = re.search(r'in', hgt)

    if units_cm:
        if 150 <= height <= 193:
            return True
    elif units_in:
        if 59 <= height <= 76:
            return True
    return False


def check_hair_color(hcl: str):
    if re.match(r'#', hcl):
        check = re.match('^[#0123456789abcdef]+$', hcl)
        return bool(check)
    return False


def check_eyes_color(ecl: str):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def check_pid(pid: str):
    if len(pid) == 9:
        check = re.match('^[0123456789]+$', pid)
        return bool(check)
    return False


data = get('https://adventofcode.com/2020/day/4/input')
passports = list(data.split('\n\n'))
count_true = 0

for passport in passports:
    passport = passport.replace('\n', ' ')
    list_data = list(passport.split(' '))
    dict_data = {}

    for l in list_data:
        try:
            k = l.split(':')[0]
            v = l.split(':')[1]
            dict_data[k] = v
        except:
            pass

    if dict_data.get('byr') and dict_data.get('iyr') and dict_data.get('eyr') and dict_data.get(
            'hgt') and dict_data.get('hcl') and dict_data.get('ecl') and dict_data.get('pid'):
        if check_year(int(dict_data['byr']), 1920, 2002) \
            and check_year(int(dict_data['iyr']), 2010, 2020) \
            and check_year(int(dict_data['eyr']), 2020, 2030) \
            and check_height(dict_data['hgt']) \
            and check_hair_color(dict_data['hcl']) \
            and check_eyes_color(dict_data['ecl']) \
            and check_pid(dict_data['pid']):
            count_true += 1

print(count_true)