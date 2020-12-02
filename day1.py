"""
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

import data

data = data.get('https://adventofcode.com/2020/day/1/input')

def find(item):
    for b in range(2021):
        try:
            a = int(item, 10)

            if a < 2021:
                if a + b == 2020:
                    if str(b) in data:
                        print(f'b={b}, a={a}, b+a={b + int(a)}, b*a={b * int(a)}')
                        break
        except:
            pass

new_data = list(map(find, data))

"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

def find_2(item):
    try:
        a = int(item, 10)
        for b in range(2021):
            if str(b) in data:
                c = 2020 - b - a
                if str(c)  in data:
                    print(a, b, c, a+b+c, a*b*c)
                    break

    except:
        pass

new_data_2 = list(map(find_2, data))