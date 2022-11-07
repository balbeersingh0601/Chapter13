#keys
L={71:'neha',42:'deepika',30:'anushka',64:'gita',15:'molly'}
lst=sorted(L)
lst1=sorted(L,reverse=True)
print("Sorted List",lst)
print("Sorted list in reverse order ",lst1)
print()
#Values
sorted_values=sorted(L.values())
print("Sorted values",sorted_values)

sorted_values=sorted(L.values(),reverse=True)
print(sorted_values)
print()

#Key-value pairs
sorted_key_value_pair=sorted((L.items()))
print("Sorted key -value pair",sorted_key_value_pair)
print()

#Max,Min and sum
numbers= {1:111,2:222,3:333,4:444}
print("Given dictionary",numbers)
print(max(numbers))
max_value=max(numbers.values())
print("Max values ",max_value)
print(min(numbers))
min_value=min(numbers.values())
print("Min values ",min_value)
print(sum(numbers))
values_sum=sum(numbers.values())
print("Sum values",values_sum)


