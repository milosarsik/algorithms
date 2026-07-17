# 682. Baseball Game

# Algorithm in English:
# 1. Initialize a stack to store valid scores.
# 2. Iterate through each operation.
#    i. If the operation is an integer, push it onto the stack.
#    ii. If the operation is "+", push the sum of the previous two scores.
#    iii. If the operation is "D", push double the previous score.
#    iv. If the operation is "C", remove the previous score.
# 3. Return the sum of the scores left in the stack.


def cal_points_stack(operations):
    # Stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    stack = []

    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


def cal_points_stack_with_temp(operations):
    # Stack with temporary pop for "+"
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    stack = []

    for op in operations:
        if op == "+":
            temp = stack.pop()
            add = temp + stack[-1]
            stack.append(temp)
            stack.append(add)
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


def cal_points_running_total(operations):
    # Stack with running total
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    stack = []
    res = 0

    for op in operations:
        if op == "+":
            score = stack[-1] + stack[-2]
            stack.append(score)
            res += score
        elif op == "D":
            score = stack[-1] * 2
            stack.append(score)
            res += score
        elif op == "C":
            res -= stack.pop()
        else:
            score = int(op)
            stack.append(score)
            res += score

    return res


operations = ["5", "2", "C", "D", "+"]

print("stack:", cal_points_stack(operations))
print("stack with temp:", cal_points_stack_with_temp(operations))
print("running total:", cal_points_running_total(operations))

operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]

print("stack:", cal_points_stack(operations))
print("stack with temp:", cal_points_stack_with_temp(operations))
print("running total:", cal_points_running_total(operations))
