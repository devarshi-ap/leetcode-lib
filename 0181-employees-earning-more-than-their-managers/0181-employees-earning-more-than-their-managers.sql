# Write your MySQL query statement below
SELECT e1.name as Employee # only need to show employee name
FROM Employee as e1
JOIN Employee as e2
ON e1.managerId = e2.id # e2 is manager
WHERE e1.salary > e2.salary