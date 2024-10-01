-- 코드를 작성해주세요
select count(id) as FISH_COUNT, month(time) as MONTH 
from fish_info
group by month(time)
order by MONTH


-- ㅇ없는 월도 출력하게 해보자
