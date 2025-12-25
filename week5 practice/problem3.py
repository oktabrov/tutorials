def zigzag_merge(list1, list2):
    max = len(list1) if len(list1) > len(list2) else len(list2); min = len(list1) if len(list1) < len(list2) else len(list2)
    empty_list = []
    for i in range(min):
        empty_list.extend([list1[i], list2[i]])
    if len(list1) != len(list2):
        if len(list1) > len(list2): empty_list.extend(list1[i+1:])
        else: empty_list.extend(list2[i+1:])
    return empty_list

a = list(input().split())
b = list(input().split())
if len(a) == len(b): print(f"Merged equal lists: {zigzag_merge(a, b)}")
elif len(a) > len(b): print(f"Merged with longer first list: {zigzag_merge(a, b)}")
else: print(f"Merged with longer second list: {zigzag_merge(a, b)}")