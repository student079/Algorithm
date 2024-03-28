-- 코드를 작성해주세요
with cte as (
    select parent_id, count(parent_id) as childs
    from ecoli_data
    group by parent_id
)

select ecoli_data.ID, ifnull(cte.childs, 0) as CHILD_COUNT
from ecoli_data left join cte
on ecoli_data.id = cte.parent_id
order by ecoli_data.ID