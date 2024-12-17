tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['G'],
    'E':['H'],
    'F':[],
    'G':[],
    'H':[],

}

stk=['A']
visited=set()

while stk:
    node=stk.pop()
    if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for neighbour in tree[node]:
            if neighbour not in visited:
                stk.append(neighbour)
