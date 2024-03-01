-- 코드를 작성해주세요
select d.dept_id as DEPT_ID,
d.DEPT_NAME_EN as DEPT_NAME_EN,
round(avg(e.SAL)) as AVG_SAL
from hr_employees as e
join hr_department as d
on e.dept_id = d.dept_id
group by d.dept_id
order by AVG_SAL desc