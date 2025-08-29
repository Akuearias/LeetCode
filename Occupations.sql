SELECT
    MAX(CASE WHEN Occupation='Doctor' THEN Name END) AS Doctor,
    MAX(CASE WHEN Occupation='Professor' THEN Name END) AS Professor,
    MAX(CASE WHEN Occupation='Singer' THEN Name END) AS Singer,
    MAX(CASE WHEN Occupation='Actor' THEN Name END) AS Actor
FROM (
    SELECT Name, Occupation,
           @rn := IF(@prev=Occupation,@rn+1,1) AS rn,
           @prev := Occupation
    FROM OCCUPATIONS, (SELECT @rn:=0,@prev:='') vars
    ORDER BY Occupation, Name
) t
GROUP BY rn;