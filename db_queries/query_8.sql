SELECT teachers.name, subjects.name, AVG(journal.grade) AS avg_grade
FROM journal 
JOIN subjects ON journal.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
GROUP BY subjects.id;