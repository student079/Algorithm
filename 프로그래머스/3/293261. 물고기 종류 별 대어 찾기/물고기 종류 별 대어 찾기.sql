-- 코드를 작성해주세요
with cte as (
    select FISH_TYPE, max(LENGTH) as ml
    from FISH_INFO
    group by FISH_TYPE
)

select fi.ID, fni.FISH_NAME, ml as LENGTH
from FISH_INFO as fi, cte
join FISH_NAME_INFO as fni
on cte.FISH_TYPE = fni.FISH_TYPE
where cte.ml = fi.length and cte.FISH_TYPE = fi.FISH_TYPE
order by fi.ID
