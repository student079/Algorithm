-- 코드를 작성해주세요

with grade as (
    select case
    when avg(g.SCORE) >= 96 then 'S'
    when avg(g.SCORE) >= 90 then 'A'
    when avg(g.SCORE) >= 80 then 'B'
    else 'C'
    end as grade, e.EMP_NO as EMP_NO
    from HR_GRADE as g
    join HR_EMPLOYEES as e
    on g.EMP_NO = e.EMP_NO
    group by e.EMP_NO
)

select e.EMP_NO, e.EMP_NAME, g.GRADE, case
when g.GRADE = 'S' then e.SAL * 0.20
when g.GRADE = 'A' then e.SAL * 0.15
when g.GRADE = 'B' then e.SAL * 0.10
else 0
end as BONUS
from HR_DEPARTMENT as d
join HR_EMPLOYEES as e
on d.DEPT_ID = e.DEPT_ID
join grade as g
on e.EMP_NO = g.EMP_NO
group by e.EMP_NO
order by e.EMP_NO