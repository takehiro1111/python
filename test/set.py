l = [3,4,9,2,5,3,7]
# for k in set(l):
#   if k % 3 == 0:
#     print(k)

for i in set(l):
    if i % 3 == 0:
        print(i)


fam = {'Takehiro','Ayumi','Chisato'}

# 要素の重複NG
# 順序が保証されない(indexの概念とは異なる)

fam.add('Yasuhiro')
fam.remove('Takehiro')

print(fam)

print(len(fam))

print("Ayumi" in fam)


# 集合→タプルへの変換
flozen_fam = frozenset(fam)
print(flozen_fam)
print(type(flozen_fam))
# flozen_fam.add('Yudai')


eng_members = ["Taro", "Jiro", "Saburo"]
math_members = ["Jiro", "Saburo", "Shiro"]

eng_members_set = set(eng_members)
math_members_set = set(math_members)

print(eng_members_set | math_members_set) # A or B(和集合)
print(eng_members_set & math_members_set) # A and B(積集合)
print(eng_members_set - math_members_set) # A  -  B (差集合)
print(math_members_set - eng_members_set) # B  -  A (差集合)

