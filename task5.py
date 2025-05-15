def number_sum(number, pair_sum):
    ans = []

    for i in range(len(number)):
        for j in range(i + 1,  len(number)):
            if number[i] + number[j] == pair_sum:
                pairs = sorted([number[i], number[j]])
                if pairs not in ans:
                    ans.append(pairs)
    return ans

number = [9,4,8,10,2,4,8,3,14,4,8]
n = 12
ans = number_sum(number, n)
print(ans)

# --------  using Binary search ------

def find_sum(numbers, pair_sum):
    numbers.sort()
    ans = []
    i = 0
    j = len(numbers) - 1

    while i < j:
        cur_sum = numbers[i] + numbers[j]
        if cur_sum == pair_sum: 
            pairs = (numbers[i], numbers[j])
            if pairs not in ans:
                ans.append(pairs)
            i += 1
            j -= 1
        elif cur_sum < pair_sum:
            i += 1
        else: 
            j -= 1
    return ans

numbers = [9,4,8,10,2,4,8,3,14,4,8]
n = 12
ans = find_sum(numbers, n)
print(ans)
