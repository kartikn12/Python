# l=[56,27,12,41,28]
# temp=0
# for i in range(len(l)):
#     for j in range(1,len(l)):
#         l[i]<l[j]
#         temp=l[i]
#         l[i]=l[j]
#         l[j]=temp
# print(temp) 

# small=0
# for i in range(len(l)):
#    for j in range(1,len(l)):
#         if l[i]<=l[j]:
#             small=l[i]
    
# print(small)
    
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             i[j]=temp
# print(temp)


# n=l[0]
# for i in l:
#     if i<n:
#         n=i
# print(n)
		


# 1 = [56,27,32,41, 16]
# n = len(L)
# min_element = 1[0]

#     for i in range(0,n):
#         if 1[i]<min_element:
#           print( min_element = 1[i])
#     for j in range(i+1,n): 
#         if 1[j] min_ element:
#             min element = 1[j]
#             print("1[j]: ",1[j])
#     1[i],min_elenent=min_element, 1[i]

#     print (min_element)
#     print (1)



L = [56, 27, 32, 41, 16]
n = len(L)

for i in range(n):  
    min_index = i                     # assume current index is minimum
    for j in range(i+1, n):           # check remaining elements
        if L[j] < L[min_index]:       # if a smaller element is found
            min_index = j             # update minimum index
    # swap the found minimum element with the first element
    L[i], L[min_index] = L[min_index], L[i]

print("Sorted List:", L)
