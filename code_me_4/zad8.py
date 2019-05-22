# Utwórz listę zawierającą wartości słownika, bez duplikatów.
#
# >>> days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
v_list = days.values()
new_list = []


for v in v_list:
    if v not in new_list:
        new_list.append(v)

print(new_list)




