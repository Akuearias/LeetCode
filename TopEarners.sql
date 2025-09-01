SELECT CONCAT(MAX(salary * months), ' ', COUNT(*)) AS result
FROM Employee
WHERE salary * months = (SELECT MAX(salary * months) FROM Employee);