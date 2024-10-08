SELECT e.name
FROM Employee e
JOIN Employee m ON e.id = m.managerId
GROUP BY e.id
HAVING COUNT(m.id) >= 5;
