SELECT
    C.company_code,
    C.founder,
    COUNT(DISTINCT L.lead_manager_code) AS lead_manager_count,
    COUNT(DISTINCT S.senior_manager_code) AS senior_manager_count,
    COUNT(DISTINCT M.manager_code) AS manager_count,
    COUNT(DISTINCT E.employee_code) AS employee_count
FROM Company C
LEFT JOIN Lead_Manager L
    ON C.company_code = L.company_code
LEFT JOIN Senior_Manager S
    ON L.lead_manager_code = S.lead_manager_code
LEFT JOIN Manager M
    ON S.senior_manager_code = M.senior_manager_code
LEFT JOIN Employee E
    ON M.manager_code = E.manager_code
GROUP BY C.company_code, C.founder;