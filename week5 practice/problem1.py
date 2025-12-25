def find_best_student(student_names, student_scores):
    if not len(student_names): return
    m = student_scores[0]; j = 0; f = False
    for i in range(len(student_scores)):
        if student_scores[i] >= m:
            f = False
            if student_scores[i] == m:
                f = True
                continue
            m = student_scores[i]
            j = i
    return student_names[j], f
    
names = list(input().split())
scores = list(map(int, input().split()))
ans = find_best_student(names, scores)
if not ans: print("Result for empty lists: None")
elif ans[1]: print(f"Top student in a tie is: {ans[0]}")
else: print(f"Top student is: {ans[0]}")