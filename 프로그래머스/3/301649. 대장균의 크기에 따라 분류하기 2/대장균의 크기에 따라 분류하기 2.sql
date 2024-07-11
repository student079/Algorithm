-- 코드를 작성해주세요
select ID, 
case
when size_rank <= ((select count(*) from ecoli_data) * 0.25) then 'CRITICAL'
when size_rank <= ((select count(*) from ecoli_data) * 0.5) then 'HIGH'
when size_rank <= ((select count(*) from ecoli_data) * 0.75) then 'MEDIUM'
else 'LOW'
end as COLONY_NAME
from 
(
    select ID, rank() over (order by size_of_colony desc) as size_rank from ecoli_data
) as size
order by ID