# Write your MySQL query statement below
SELECT
    e1.name as Employee # only need to show employee name
FROM
    Employee as e1 # e1=emp
JOIN
    Employee as e2 # e2=manager
ON
    e1.managerId = e2.id
WHERE
    e1.salary > e2.salary