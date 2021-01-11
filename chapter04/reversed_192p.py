list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

print("# reversed() function")
print("reversed([1,2,3,4,5]):", list_reversed)
print("list(reveresed([1,2,3,4,5])):", list(list_reversed))
print()

print("# reversed() function and repetition")
print("for i in reversed(([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-", i)