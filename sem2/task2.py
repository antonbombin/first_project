"""
Задача №3. Решение в группах Напишите программу для
печати всех уникальных значений в словаре.
Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
         {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
         {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

sp = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# традиционный итератор с методов add()
unique_values = set()
for i in sp:
    for key, value in i.items():
        unique_values.add(value.strip())
print(unique_values)


