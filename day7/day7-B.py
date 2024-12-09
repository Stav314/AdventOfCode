from itertools import product


input_data = []
with open("day7/input.txt", 'r') as file:
    for line in file:
        test_value, numbers = line.split(':')
        numbers = list(map(int, numbers.split()))
        input_data.append((int(test_value), numbers))

ans = 0

for test_value, numbers in input_data:
    num_operators = len(numbers) - 1
    
    for operators in product(['+', '*', '||'], repeat=num_operators):

        result = numbers[0]

        for i, op in enumerate(operators):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            elif op == '||':
                result = int(str(result) + str(numbers[i + 1]))

        if result == test_value:
            ans += test_value
            break

print(ans)
