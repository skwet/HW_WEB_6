SELECT groups.name,subjects.name,round(AVG(journal.grade), 2) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN journal ON students.id = journal.student_id
JOIN subjects ON journal.subject_id = subjects.id
GROUP BY groups.id, subjects.id;