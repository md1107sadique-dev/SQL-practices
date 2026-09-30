SELECT C.name AS customers
FROM Customers AS C
LEFT JOIN Orders AS O
ON C.id = O.customerId
    WHERE O.customerId IS NULL;