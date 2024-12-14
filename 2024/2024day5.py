from aocd import data

# data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

rules_raw, books = data.split("\n\n")

rules = []
for line in rules_raw.split("\n"):
    
    rules.append(tuple(map(int, line.split("|"))))

def fix(pages, page_num):
    while True:
        for rule in rules:
            try:
                first = page_num[rule[0]]
                second = page_num[rule[1]]
            except KeyError:
                pass
            else:
                if second < first:
                    pages[first], pages[second] = pages[second], pages[first]
                    page_num[rule[0]] = second
                    page_num[rule[1]] = first
                    print(pages)
                    break
        else:
            return

part1 = 0
part2 = 0
for line in books.split("\n"):
    pages = list(map(int, line.split(",")))
    page_num = {}
    for i, page in enumerate(pages):
        page_num[page] = i
    for rule in rules:
        try:
            first = page_num[rule[0]]
            second = page_num[rule[1]]
        except KeyError:
            pass
        else:
            if second < first:
                fix(pages, page_num)
                part2 += pages[len(pages) // 2]
                break
    else:
        part1 += pages[len(pages) // 2]
        
print(part1)
print(part2)
    