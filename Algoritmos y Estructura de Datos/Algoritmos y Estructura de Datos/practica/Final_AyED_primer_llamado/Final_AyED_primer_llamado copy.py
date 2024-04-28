class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(3)
root.left.left = Node(10)
root.left.right = Node(5)
root.left.right.left = Node(4)
root.left.right.right = Node(33)
root.right = Node(13)
root.right.right = Node(7)
root.right.right.left = Node(23)
root.right.right.right = Node(1)

def calcular(node):
    if node is None:
        return float("-inf"), float("inf"), 0, 0
    
    max_value = node.value
    min_value = node.value
    sum_value = node.value
    count = 1

    if node.left is not None:
        left_max, left_min, left_sum, left_count = calcular(node.left)
        max_value = max(max_value, left_max)
        min_value = min(min_value, left_min)
        sum_value += left_sum
        count += left_count

    if node.right is not None:
        right_max, right_min, right_sum, right_count = calcular(node.right)
        max_value = max(max_value, right_max)
        min_value = min(min_value, right_min)
        sum_value += right_sum
        count += right_count

    average = sum_value / count

    return max_value, min_value, average, count

max_value, min_value, average, count = calcular(root)

print("El valor máximo es:", max_value)
print("El valor mínimo es:", min_value)
print("El valor promedio es:", average)
print("\n")
