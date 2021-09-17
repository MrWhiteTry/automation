import random

def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert


# Проверяем, что оно работает
randomListOfNums = []
while len(randomListOfNums) < 20:
    randomListOfNums.append(random.randint(0, 100))
print(randomListOfNums)
insertion_sort(randomListOfNums)
print(randomListOfNums)