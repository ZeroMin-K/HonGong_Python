power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("After map")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("After filter")
print("filter(under_3, output_b):", output_b)
print("filter(under_3, output_b):", list(output_b))