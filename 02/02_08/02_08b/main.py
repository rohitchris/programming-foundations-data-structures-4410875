# my_list = [1, 7, 3, 0,9,15,423,2,1,42,2,2,2,4]
# print(sorted(my_list, reverse=True))



student_grades = [('Sarah', 89), ('Rebecca', 82), ('Andy', 99), ('Matt', 71)]
print(sorted(student_grades, key=lambda x:x[1]))

# print(sorted(student_grades, key=lambda x:x[1], reverse=True))
