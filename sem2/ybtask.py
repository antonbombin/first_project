my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]
all_ratings = my_ratings + other_ratings
print(all_ratings)
#операции со списком
print(min(all_ratings))
print(max(all_ratings))
print(sum(all_ratings)/len(all_ratings))
#сортировка
all_ratings.sort()
print(all_ratings)

#срез
ratings = [2.5, 5.0, 4.3, 3.7, 4.5]

first_two_ratings = ratings[:2]
print(first_two_ratings)

middle_ratings = ratings[1:-1]
print(middle_ratings)

last_two_ratings = ratings[-2:]
print(last_two_ratings)




