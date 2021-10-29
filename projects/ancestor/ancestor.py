# # First Pass Solution
# def earliest_ancestor(ancestors, starting_node):

#     q = [[starting_node]]

#     paths = []

#     while len(q) > 0:
#         path = q.pop(0)
#         cur_node = path[-1]
#         count = 0
#         for ancestor in ancestors:
#             if ancestor[1] == cur_node:
#                 q.append(list(path) + [ancestor[0]])
#                 count += 1
#         if count == 0 and len(path) > 1:
#             paths.append(path)
    
#     paths.sort(key=len)

#     if len(paths) == 0:
#         return -1
#     else:
#         result = []
#         for path in paths:
#             if len(path) == len(paths[-1]):
#                 result.append(path[-1])
    
#         return sorted(result)[0]

# uses dictionary to spend less time iterating through lists
def earliest_ancestor(ancestors, starting_node):

    q = [[starting_node]]

    paths = []

    children = {}

    for ancestor in ancestors:
        if ancestor[1] in children:
            children[ancestor[1]] += [ancestor[0]]
        else:
            children[ancestor[1]] = [ancestor[0]]
    
    while len(q) > 0:
        path = q.pop(0)
        cur_node = path[-1]
        count = 0
        if cur_node in children:
            for parent in children[cur_node]:
                q.append(list(path) + [parent])
                count += 1
        if count == 0 and len(path) > 1:
            paths.append(path)
                
    paths.sort(key=len)

    if len(paths) == 0:
        return -1
    else:
        result = []
        for path in paths:
            if len(path) == len(paths[-1]):
                result.append(path[-1])
    
        return sorted(result)[0]