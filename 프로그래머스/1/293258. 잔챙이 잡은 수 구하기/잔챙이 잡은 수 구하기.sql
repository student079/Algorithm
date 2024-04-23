-- 코드를 작성해주세요
# null 개수 세기

select count(*) as FISH_COUNT
from fish_info
where isnull(length)