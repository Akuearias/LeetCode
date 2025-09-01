alter table EMPLOYEES
add column Salary_wrong int unsigned;

update EMPLOYEES
set Salary_wrong = cast(replace(Salary, '0', '') as unsigned);

select ceil(avg(Salary) - avg(Salary_wrong)) from EMPLOYEES;