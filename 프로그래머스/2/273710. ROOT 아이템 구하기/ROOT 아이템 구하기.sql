-- 코드를 작성해주세요
select i.item_id, i.item_name
from ITEM_INFO as i
join ITEM_TREE as t
on i.item_id = t.item_id
where t.parent_item_id is null
order by i.item_id