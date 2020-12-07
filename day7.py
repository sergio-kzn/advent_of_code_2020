"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

Your puzzle answer was 229.

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

Your puzzle answer was 6683.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Share] this puzzle.
"""
import re

import data

raw_data = data.get('https://adventofcode.com/2020/day/7/input')
raw_data.remove('')

BAG = 'shiny gold'


def replace_list_to_dict(str):
    """создаем словарь, где ключ - сумка, а значения - список из сумок, которые можно хранить"""
    rule_dict = dict({str.split(' bags contain ')[0]: str.split(' bags contain ')[1]})
    for k, v in rule_dict.items():
        # убираем лишние слова и символы
        v = re.sub(r' bag[s]*', '', v)
        v = re.sub(r'\.', '', v)

        rule_dict[k] = list(v.split(', '))
    return rule_dict


new_data = list(map(replace_list_to_dict, raw_data))

true_colors = set()


def search_color(bag: str):
    """добавляем в сет те сумки, в которые можно положить *bag*"""
    for rule in new_data:  # проходимся по всем правилам
        for key_bag, list_rule_for_bag in rule.items():  # правило состоит из ключа (сумки) и значения (возможные сумки)
            for rule_for_bag in list_rule_for_bag:  # перебираем все значения (возможные сумки)
                if re.search(bag, rule_for_bag):
                    true_colors.add(key_bag)


search_color(BAG)  # первый прогон функции, чтобы заполнить начальными значениями наш сет

# делаем цикл, до тех пор, пока наш сет не перестанет наполнятся
test_true_colors = set()
while test_true_colors != true_colors:
    test_true_colors = true_colors.copy()
    for bag in test_true_colors:
        search_color(bag)

print(len(true_colors))  # 229

##################################
#             part 2             #
##################################


true_bags = dict({BAG: {
    'count': 1,
    'items': {},
}})


def fill_dict_2(obj, key):
    """
    сделаем дерево на основе словаря.
    +-- наша сумка
    |   +-- название или цвет сумки
    |   +-- количество
    |   +-- другие сумки, которые можно поместить в эту сумку
    |   |   +-- название
    |   |   +-- количество
    |   |   +-- другие сумки, которые можно поместить в эту сумку
    ...
    И так пока не встретим no other
    """

    for data in new_data:
        if data.get(key):
            for list_item in data.values():
                for item in list_item:
                    if item != 'no other':
                        new_key = re.sub(r'\d+\s', '', item)
                        count = int(re.match(r'\d+', item).group(0))
                        obj[key]['items'][new_key] = {}
                        obj[key]['items'][new_key]['count'] = count
                        obj[key]['items'][new_key]['items'] = {}
                        fill_dict_2(obj[key]['items'], new_key)


def calc_sum(obj, key):
    """вычесляем сумму всех пакетов в каждой ветке нашего дерева"""
    global all_summ
    if obj[key]['items']:
        for item in obj[key]['items']:
            obj[key]['items'][item]['summ'] = obj[key]['items'][item]['count']
            calc_sum(obj[key]['items'], item)
        obj[key]['summ'] = sum((obj[key]['items'][item]['summ']) for item in obj[key]['items'])
        obj[key]['summ'] *= obj[key]['count']
        obj[key]['summ'] += obj[key]['count']


fill_dict_2(true_bags, BAG)
calc_sum(true_bags, BAG)
print(true_bags['shiny gold']['summ'] - 1)  # -1, потому что нашу сумку мы не учитываем

# посмотреть дерево в консоли
# from pprint import pprint
# pprint(true_bags)
