import random
list_length = 25
max_value = 50
min_value = 1
threshold = 10
result_list = []

for number in [random.randint(min_value, max_value) for _ in range(list_length)]:
    if number > threshold:
        result_list.append(number)
    else:
        print("Ignoring", number)
print(result_list)
