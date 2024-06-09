# scores = [62, 91, 84]

scores = {"math": 62, "english": 91, "physics": 84}

# scores["math"] = 100
# scores["chemistry"] = 40

# del scores["english"]
popped_value = scores.pop("english")

print(scores)
# print(scores["english"])
print(popped_value)


# for文との組み合わせ
scores = {"math": 62, "english": 91, "physics": 84}

for key in scores.keys():
    print(key)

for value in scores.values():
    print(value)
    
for k,v in scores.items():
    print(f'{k}:{v}')
