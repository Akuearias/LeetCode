select name as Customers from Customers left join Orders on Orders.customerId = Customers.id
where Orders.customerId is null