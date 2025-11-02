def changeTree(root): 
    if not root or (not root.left and not root.right):
        return 
    
    left_val = root.left.data if root.left else 0
    right_val = root.right.data if root.right else 0

    if left_val + right_val < root.data:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data
    changeTree(root.left)
    changeTree(root.right)
    
    left_val = root.left.data if root.left else 0
    right_val = root.right.data if root.right else 0
    root.data = left_val + right_val
    return root

''' 
  time complexity : O(n)
  space complexity : O(h)
'''
