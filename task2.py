names=['Smith', 'Johnson', 'Williams', 'Jones','Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Andreson', 'Thomas', 'Jackson', 'White']

name_length = [len(name) for name in names]


name_length1 = {}
for name in names:
    length = len(name)
    if length not in name_length1:
        name_length1[length] = []
    name_length1[length].append(name)


length_freq = {}
for length in name_length1:
    length_freq[length] = len(name_length1[length])
    
sorted_length = sorted(length_freq.items(), key = lambda x: x[1], reverse=True)

common_name = sorted_length[:3]
common_least = sorted_length[-3:]


print(f"Names : {', '.join(names)}")
print(f"Name : {name_length}")
print("\n The Three most frequent name lengths are : ")
count = 0
for length, freq in common_name:
    count += 1
    print(f"{freq} Name of length {length} : {name_length1[length]}")

print("\n The Three least frequent name lengths are : ")
count = 0
for length, freq in common_least:
    count +=1
    print(f"{freq} Name of length {length} : {name_length1[length]}")







