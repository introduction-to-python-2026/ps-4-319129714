def split_before_each_uppercases(formula):
    if not formula:
        return []
        
    start = 0
    split_formula = []
    
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
            
    split_formula.append(formula[start:len(formula)])
    
    return split_formula

def split_at_first_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric_str = formula[digit_location:] 
        numeric_int = 0
        if numeric_str:
            try:
                numeric_int = int(numeric_str)
            except ValueError:
                pass
        return prefix, numeric_int
