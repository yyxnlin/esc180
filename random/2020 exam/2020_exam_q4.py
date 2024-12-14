def get_target_noparens(nums, target):
    operations = ["+", "-", "*", "/"]
    nums_in_order = get_perms(nums)
    op_orders = get_operations(len(nums)-1, operations)

    print(nums_in_order)
    res = None

    for i in range (len(nums_in_order)):
        
        numbers = nums_in_order[i]


        for k in range (len(op_orders)):
            expression = ""
            exp = []
            opers = op_orders[k]

            for j in range (len(numbers)-1):
                exp.append(numbers[j])
                exp.append(opers[j])
                expression += str(numbers[j]) + " " + str(opers[j]) + " "
            
            exp.append(numbers[-1])
            expression += str(numbers[-1])

            print (exp)
            res = eval_exp(exp)
            print(res)
            if (res == target):
                return expression
        
def get_perms(list):
    if (len(list) == 1):
        return [list]
    
    res = []
    for ind in range (len(list)):
        rem_perms = get_perms(list[0:ind] + list[ind+1:])

        for i in range (len(rem_perms)):
            res.append([list[ind]] + rem_perms[i])
        
    return res

def get_operations(num_ops, ops):
    if (num_ops == 0):
        return []
    
    res = []

    for i in range (len(ops)):
        cur = [ops[i]]
        cur.extend(get_operations(num_ops-1, ops))
        res.append(cur)
    print (res)
    return res

def eval_exp(exp):
    exp2 = [exp[0]]
    i = 1

    while (i < len(exp)-1):
        if (exp[i] == "*"):
            exp2.append(exp[i-1] * exp[i+1])
            i+=2
        elif (exp[i] == "/"):
            exp2.append(exp[i-1] / exp[i+1])
            i+=2
        else:
            exp2.append(exp[i])
            i += 1
    exp2.append(exp[-1])

    i = 0
    res = exp2[0]
    while (i < len(exp2)-1):
        if (exp[i] == "+"):
            res += exp2[i+1]
        elif (exp[i] == "-"):
            res -= exp2[i+1]
        i+=1

    return res

print(get_target_noparens([3, 1, 2], 7))