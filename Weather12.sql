select distinct CITY from STATION
where (upper(left(CITY, 1)) not in ('A', 'E', 'I', 'O', 'U')) and (upper(right(CITY, 1)) not in ('A', 'E', 'I', 'O', 'U'))