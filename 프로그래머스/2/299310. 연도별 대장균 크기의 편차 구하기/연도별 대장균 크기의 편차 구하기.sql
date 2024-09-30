-- 코드를 작성해주세요

with year_maxsize as (
select year(differentiation_date) as year, max(size_of_colony) as max_size
from ecoli_data
group by year(differentiation_date)
    )

select year(e.differentiation_date) as YEAR, y.max_size-e.size_of_colony as YEAR_DEV, e.id as ID
from ecoli_data as e
join year_maxsize as y
on year(e.differentiation_date) = y.year
order by YEAR asc, YEAR_DEV asc

