SELECT teachers.name,subjects.name, students.name
FROM subjects
JOIN journal ON journal.subject_id = subjects.id
JOIN students ON students.id = journal.student_id
JOIN teachers ON teachers.id = subjects.teacher_id
WHERE students.id = 1 AND teachers.id = 1
GROUP BY subjects.name