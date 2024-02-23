with new_table as 
(SELECT 
    CASE 
        WHEN skill_code & (SELECT SUM(code) FROM skillcodes WHERE category = 'Front End') AND 
             skill_code & (SELECT code FROM skillcodes WHERE name = 'Python') THEN 'A'
        WHEN skill_code & (SELECT code FROM skillcodes WHERE name = 'C#') THEN 'B'
        WHEN skill_code & (SELECT SUM(code) FROM skillcodes WHERE category = 'Front End') THEN 'C'
    END AS GRADE, 
    ID, 
    EMAIL
FROM 
    DEVELOPERS
ORDER BY 
    GRADE, 
    ID
 )

select * from new_table where GRADE IS NOT NULL