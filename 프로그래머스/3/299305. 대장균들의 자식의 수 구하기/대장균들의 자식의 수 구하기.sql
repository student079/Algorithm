-- 코드를 작성해주세요
with id_count as (
select a.id as ID, count(*) as count
from ecoli_data as a
join ecoli_data as b
on a.id = b.parent_id
group by a.id
    )
    
select e.id as ID, ifnull(ic.count, 0) as CHILD_COUNT
from ecoli_data as e
left outer join id_count as ic
on e.id = ic.id
order by ID