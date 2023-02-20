# s = str(input())
# a = 1
# while a < len(s):
#     a *= 2
# buff = ['-', -1, -1, -1, -1, -1, -1]
# tree = [buff.copy() for i in range(a - 1)]
# for i in range(a):
#     if i < len(a):
#         tree.append([s[i], i, i, i, a + i // 2, -1, -1])
#     else:
#         tree.append(['_', i, i, i, a + i // 2, -1, -1])
# for i in range(2 * a - 1 -1, -1, -1):
#     if tree[tree[i][4]][0] == '-':
#         tree[tree[i][4]][0] = tree[i][0]
#         tree[tree[i][4]][3] = tree[i][3]
#         tree[tree[i][4]][6] = tree[i][1]
#     elif tree[tree[i][4]][0] == '_':
#         tree[tree[i][4]][0] = tree[i][0]
#         tree[tree[i][4]][2] = tree[i][2]
#         tree[tree[i][4]][5] = tree[i][1]
#     else:
#         if tree[tree[i][4]][0] > tree[i][0]:
#             tree[tree[i][4]][0] = tree[i][0]
#         tree[tree[i][4]][2] = tree[i][2]

n, k = list(map(int, input().split()))
s = list(map(int, input().split()))

t = range(n)
def rec(e):
    su = 1
    for i in range(len(e)):
        for j in range(len(e)):
            for k in range(len(e)):
                if i != j and i != k and j != k:
                    if (s[e[j]] == e[i] and s[e[k]] == e[i]) and  (s[e[i]] == e[j] and s[e[k]] == e[j]) and  (s[e[j]] == e[k] and s[e[i]] == e[k]):
                        q = [i, j, k]
                        q.sort()
                        e1 = e.copy()
                        e1.pop(q[0])
                        e1.pop(q[1]-1)
                        e1.pop(q[2]-2)
                        su *= rec(e1)
    return su
print(rec(t))