SELECT groups.name, students.id, students.name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.id = 1
ORDER BY students.id