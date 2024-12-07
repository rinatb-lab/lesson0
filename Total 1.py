grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
#print(students)
#print(grades)
student_results={}
while len(grades)>0:
    result=grades.pop(0)
    student=students.pop(0)
    n=len(student)
    result=sum(result)/n
    #print(student,':',result)
    student_results.update({student:result})
print(student_results)