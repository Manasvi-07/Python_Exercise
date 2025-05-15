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
    