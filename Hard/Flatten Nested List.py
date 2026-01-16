
#CASE A-when result is a local variable for printing print(flatten_local([1, [2, 3]])) print(flatten_local([4, [5]]))
#for output[1, 2, 3] [4, 5]
def flatten_local(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_local(item))
        else:
            result.append(item)
    return result


#CASE B-when the result is a global  for flatten_global([1, [2, 3]]) flatten_global([4, [5]]) 
#for output [1, 2, 3, 4, 5]  

result = []

def flatten_global(nested):
    for item in nested:
        if isinstance(item, list):
            flatten_global(item)
        else:
            result.append(item)

