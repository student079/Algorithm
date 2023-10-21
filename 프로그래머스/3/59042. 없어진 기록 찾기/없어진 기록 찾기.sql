# 레프트 아우터 조인 활용
select o.animal_id as ANIMAL_ID, o.name as NAME
from animal_outs as o left outer join
animal_ins as i on o.animal_id = i.animal_id
where i.animal_id is null
order by o.animal_id