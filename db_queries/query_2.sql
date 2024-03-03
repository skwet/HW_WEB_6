SELECT students.id, students.name, AVG(journal.grade) AS avg_grade
FROM students 
JOIN journal ON students.id = journal.student_id
WHERE journal.subject_id = 1
GROUP BY students.id, students.name
ORDER BY avg_grade DESC
LIMIT 1;