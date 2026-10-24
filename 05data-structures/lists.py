#list

#list powers : mutable, duplicates, ordered, heterogenous

# a = [1, 2, 3, 4.3, 5, True, "Hello", print(), 2]
# a[0] = 99
# print(a)

#1st way using index
# b = [1, 2, 3, 4.3, 5, 6]
# for i in range(len(b)):
#     print(b[i])

#2nd way directly on values
# for i in b:
#     print(i)

#functions vs methods
# print(dir(list))

# l = [1, 2, 3, 4, 5]
# l.append(6)
# l.append(7)
# print(l)

# l.insert(2, 21)
# print(l)

# l.extend([9, 10, 11])
# print(l)

# l.remove(1)
# print(l)

#List Practice Ques

# a = [6, -89, 9, 2, -98, -6]
# print("Positive numbers are: ")
# for i in a:
#     if i >= 0: print(i)

# print("Negative numbers are: ")
# for i in a:
#     if i<0: print(i)

# b = [2, 4, 6, 8, 10]
# sum = 0
# for i in b:
#     sum = sum+i
# mean = sum/len(b)
# print(mean)

# c = [1, 2, 32, 444, 56, 999]
# greatest = c[0]
# index = 0
# for i in range(len(c)):
#     if c[i] > greatest: greatest = c[i]
#     index = i
# print(f"Greatest number of the list is {greatest} and it's index is {index}.")

# d = [1, 2, 3, 4, 66, 88, 999, 98, 2]
# greatest = d[0]
# sec_greatest = d[0]

# for i in range(len(d)):
#     if d[i] > greatest: 
#         sec_greatest = greatest
#         greatest = d[i]
#     elif d[i] > sec_greatest:
#         sec_greatest = d[i]
# print(greatest, sec_greatest)

e = [33, 99, 1, 2, 34, 5]
for i in range(len(e)-1):
    if e[i] < e[i+1]:
        continue
    else: 
        print("Your list is not sorted!")
        break
else: print("Your list is sorted!")