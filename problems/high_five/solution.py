class Solution:
    def highFive(self, grades: List[List[int]]) -> List[List[int]]:
        student_grades = {}
        for student, grade in grades:
            if student not in student_grades:
                student_grades[student] = []
            student_grades[student].append(grade)
        return [
            [student, sum(sorted(student_grades[student], reverse=True)[:5]) // 5]
            for student in sorted(student_grades.keys())
        ]