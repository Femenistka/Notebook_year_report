vector = [2,5,9,7,4,1]
for j in range(len(vector)):
    for i in range(len(vector)):
    
        current_el = vector[i]
    
        if i == len(vector) - 1:
            continue

        next_el = vector[i + 1]
        if current_el > next_el:
            vector[i] = next_el
            vector[i+1] = current_el 

        

        

print(vector)