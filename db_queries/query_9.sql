SELECT students.name, subjects.name 
FROM journal 
JOIN students ON students.id = journal.student_id
JOIN subjects ON subjects.id = journal.subject_id
GROUP BY students.name