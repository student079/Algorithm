-- 코드를 작성해주세요
with recursive ecoli_gene as (
    select id, parent_id, 1 as GENERATION
    from ecoli_data
    where isnull(parent_id)
    
    union all (
    select 
        e.id, e.parent_id, eg.generation + 1 as GENERATION
        from ecoli_data as e
        join ecoli_gene as eg
        on eg.id = e.parent_id
    )
)

select count(id) as COUNT, GENERATION
from ecoli_gene as eg
where id not in 
(
select parent_id
from ecoli_data
where parent_id is not null
)
group by eg.GENERATION