-- 코드를 작성해주세요
select count(id) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE
from FISH_INFO
group by fish_type
having avg(ifnull(length, 10)) >= 33
order by FISH_TYPE