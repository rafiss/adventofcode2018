num_recipes = 939601

recipes = [3, 7]

elf_a_pos = 0
elf_b_pos = 1

while len(recipes) < num_recipes + 11:
    s = recipes[elf_a_pos] + recipes[elf_b_pos]
    new_1 = s % 10
    new_2 = s / 10
    if new_2 > 0:
        recipes.append(new_2)
    recipes.append(new_1)
    elf_a_pos = (elf_a_pos + 1 + recipes[elf_a_pos]) % len(recipes)
    elf_b_pos = (elf_b_pos + 1 + recipes[elf_b_pos]) % len(recipes)

print recipes[9:19]
print recipes[num_recipes:num_recipes+10]
#print ''.join(recipes[num_recipes:num_recipes+10])
