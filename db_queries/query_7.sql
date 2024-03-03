SELECT students.name, journal.grade
FROM journal
JOIN students ON journal.student_id = students.id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON journal.subject_id = subjects.id
WHERE groups.id = 1 AND subjects.id = 1;