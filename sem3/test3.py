k = 'ноутбук'
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# Это 2 словаря где Цифры это Ключи(<class'int'>)
#  Буквы это Значения(<class'str'>)
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM': # Английский алфавит набранный на клавиатуре
        for j in points_en:
            if i in points_en[j]: # если искомая буква есть в Значении из англ. словаря
                count = count + j # то мы прибавляем Ключ этого значения
    else: # Если i Английском алфавите, то обращаемся к Русскому словарю
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j # по скольку Ключи типа int их можно сразу складывать
print(count)