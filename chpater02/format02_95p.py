# Integer
output_a = "{:d}".format(52)

# print specific space
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# fill 0 in space
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# Basic")
print(output_a)
print("#print specific space")
print(output_b)
print(output_c)
print("# fill 0 in space")
print(output_d)
print(output_e)