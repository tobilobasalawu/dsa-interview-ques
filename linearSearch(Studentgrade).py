'''
Edge Cases

1. if student in the list
2. if student not in the list
3. if student name appears more than once
4. if student name appears at the beginning of the list
5. if student name apeears at the end of the list
6. if the student name appears at the miidle of the list

pseudocde

if the students is in the list:
    show the student grades
and if it is not in the list
    show student not found

'''

test_cases = [
    
    {
        'input' : {
            'students' : ["Alice", "Bob", "Charlie", "David", "Eve"],
            'grades' : [90, 672, 78, 990, 688],
            'search_student' : "Charlie"
        }, 'output' : 78
    },
    
    {
            'input' : {
                'students' : ["Alice", "Bob", "Charlie", "David", "Eve"],
                'grades' : [85, 92, 78, 90, 88],
                'search_student' : "Frank"
        }, 'output' : 'Student not Found'
    },
    
        {
            'input' : {
                'students' : ["Alice", "Bob", "Charlie", "David", "Eve"],
                'grades' : [85, 92, 78, 90, 88],
                'search_student' : "Alice"
        }, 'output' : 85
    },
    
    {
        'input' : {
                'students' : ["Alice", "Bob", "Charlie", "David", "Eve"],
                'grades' : [85, 92, 78, 90, 88],
                'search_student' : "Eve"
        }, 'output' : 88
    },
    
    {
        'input' : {
                'students' : ["Alice", "Bob", "Charlie", "Alice", "Eve"],
                'grades' : [85, 92, 78, 90, 88],
                'search_student' : "Alice"
        }, 'output' : 85
    },
    
    
]

def find_student_grade(students, grades, search_student):
    
    if search_student in students:
        position = students.index(search_student)
        return grades[position]
    
    else:
        return 'Student not Found'
    
for i, test_case in enumerate(test_cases):
    result = find_student_grade(**test_case['input'])
    expected = test_case['output']
    print('Passed ✅') if result == expected else print('Failed ❌')



