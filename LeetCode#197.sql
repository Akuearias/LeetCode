select w1.id as Id from Weather w1
join Weather w2 on w2.recordDate = date_sub(w1.recordDate, interval 1 day) and w2.temperature < w1.temperature