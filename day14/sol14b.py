target = 939601
#target = 92510

recipes = [3, 7]

elf_a_pos = 0
elf_b_pos = 1

def l_to_num(l):
    return ''.join([str(i) for i in l])
print l_to_num(recipes)

while str(target) not in l_to_num(recipes[-10:]):
    s = recipes[elf_a_pos] + recipes[elf_b_pos]
    new_1 = s % 10
    new_2 = s / 10
    if new_2 > 0:
        recipes.append(new_2)
    recipes.append(new_1)
    elf_a_pos = (elf_a_pos + 1 + recipes[elf_a_pos]) % len(recipes)
    elf_b_pos = (elf_b_pos + 1 + recipes[elf_b_pos]) % len(recipes)

target_len = len(str(target))
print len(recipes) - target_len - (0 if l_to_num(recipes[-target_len:]) == str(target) else 1)
#print recipes[-10:]
