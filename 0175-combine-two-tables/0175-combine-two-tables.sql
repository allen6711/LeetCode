# Write your MySQL query statement below
SELECT a.firstName, a.lastName, b.city, b.state
FROM Person as a left join Address as b
ON a.personId = b.personID