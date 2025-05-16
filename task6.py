def count_Substring(string, substring):
    count = 0
    for i in range(len(string) - len(substring)+1):
        if string[i : i + len(substring)] == substring:
            count += 1
    return count

string = "PQRQRQRQ"
substring = "QRQ"
print(count_Substring(string, substring))