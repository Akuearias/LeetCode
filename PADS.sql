select concat(Name, '(', left(Occupation, 1), ')') as name from OCCUPATIONS order by Name;

select concat("There are a total of ", count(Occupation), ' ', lower(Occupation), 's.') as msg from OCCUPATIONS group by Occupation order by count(Occupation) asc, Occupation asc;