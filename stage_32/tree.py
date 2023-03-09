def preorder(i, n):
    if tree[i]:
        stack1.append(tree[i])
        preorder(2 * i, n)
        preorder(2 * i + 1, n)

def inorder(i, n):
    if tree[i]:
        preorder(2 * i, n)
        stack2.append(tree[i])
        preorder(2 * i + 1, n)

def postorder(i, n):
    if i < n:
        preorder(2 * i, n)
        preorder(2 * i + 1, n)
        stack3.append(tree[i])

N = int(input())
stack1 = []
stack2 = []
stack3 = []
tree = [0]*(2**N + 1)
for _ in range(N):
    p, lc, rc = map(str, input().split())
    if p == 'A':
        tree[ord('A')-64] = p
        if lc != '.':
            tree[(ord(p) - 64) * 2] = lc
        if rc != '.':
            tree[(ord(p) - 64) * 2 + 1] = rc
    else:
        if lc != '.':
            tree[(ord(p) - 64) * 2] = lc
        if rc != '.':
            tree[(ord(p) - 64) * 2 + 1] = rc

preorder(1, len(tree))
inorder(1, len(tree))
# postorder(1, len(tree))

print(*stack1)
print(*stack2)