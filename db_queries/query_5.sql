SELECT teachers.name, subjects.name AS subject
FROM teachers 
JOIN subjects ON subjects.teacher_id = teachers.id
ORDER BY teachers.id;