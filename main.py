import heapq

# вхідні дані з довжинами кабелів
numbers = [5, 8, 4, 2, 9, 1, 7, 6, 3]
# створимо купу з цих даних
heapq.heapify(numbers)
# поєднаємо кабелі беручі з купи кожен раз два найкоротші
heap_length = len(numbers)
total_cost = 0
current_cost = 0
while heap_length > 1:
    min_element_1 = heapq.heappop(numbers)
    min_element_2 = heapq.heappop(numbers)
    current_cost = min_element_1 + min_element_2
    heapq.heappush(numbers, current_cost)
    total_cost += current_cost
    heap_length -= 1
# вивдемо отриманий результат
print(total_cost)
