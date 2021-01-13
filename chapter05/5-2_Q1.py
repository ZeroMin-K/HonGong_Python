def flatten(data):
    output = []
    for elem in data: 
        if type(elem) == list:
            output += flatten(elem)
        else:
            output.append(elem) 
    
    return output

example = [[1,2,3],[4,[5,6]], 7, [8,9]]
print("Original:", example)
print("Convert:", flatten(example))