def height(root):
    if root is None:
        return 0
    hleft = 0
    hright = 0
    if root.left:
        hleft = 1 + height(root.left)
    if root.right:
        hright = 1 + height(root.right)
    if hleft > hright:
        return hleft + 1
    return hright+1

def levelOrder(root):
    ht = height(root)
    for i in range(1,ht+1):
        printLevel(root, i)

def printLevel(root, level):
    if root is None:
        return root
    if level == 1:
        print(root.info, end=' ')
    printLevel(root.left, level-1)
    printLevel(root.right, level-1)
