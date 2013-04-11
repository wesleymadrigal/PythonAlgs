# an algorithm I devised to find the longest repetition within a list
# if said list has more than one longest repetition the element
# which appears first in the list is returned


def longest_repetition(L):
    if len(L) == 0:
        return None
    else:
        count = 1
        previous = L[0]
        counts = {}
        for i in range(1,len(L)):
            if L[i] == previous:
                count += 1
                previous = L[i]
            else:
                counts[str(previous)] = count
                count = 1
                previous = L[i]
        counts[str(previous)] = count
        biggest = max([y for x, y in counts.items()])
        # this portion is to insure that we return the first
        # appearance of a big repetition when we have multiple
        keys_and_indexes = {}
        for e in counts.keys():
            if counts[e] == biggest:
                if e.isdigit():
                    keys_and_indexes[e] = L.index(int(e))
                elif e.isalpha():
                    keys_and_indexes[e] = L.index(e)
        return min([x for x,y in keys_and_indexes.items()])
        
        
# a better version

def longest_repetition(input_list):
    best_element = None
    length = 0
    current = None
    current_length = 0
    for element in input_list:
            if current != element:
                    current = element
                    current_length = 1
            else:
                    current_length = current_length + 1
            if current_length > length:
                    best_element = current
                    length = current_length
    return best_element
    
    
