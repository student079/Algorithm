-- 코드를 작성해주세요
select sum(g.score) as SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_GRADE as g join
HR_EMPLOYEES as e on
g.EMP_NO = e.EMP_NO
group by e.EMP_NO
order by sum(g.score) desc
limit 1