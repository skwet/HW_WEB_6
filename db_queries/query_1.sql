SELECT students.id, students.name, AVG(journal.grade) AS avg_grade
FROM students
JOIN journal ON students.id = journal.student_id
GROUP BY students.id, students.name
ORDER BY avg_grade DESC
LIMIT 5;