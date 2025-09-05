delete p from Person p
join Person p2
on p.email = p2.email and p.id > p2.id