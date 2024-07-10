-- 코드를 작성해주세요
# 임시 테이블
with recursive ecoli_gene as (
    select id, parent_id, 1 as GE
    from ecoli_data
    where parent_id is null
    
    union all 
    (
    select d.id, d.parent_id, g.ge + 1
        from ecoli_gene as g
        join ecoli_data as d
        on g.id = d.parent_id
    )
)

select id from ecoli_gene
where ge = 3
order by id