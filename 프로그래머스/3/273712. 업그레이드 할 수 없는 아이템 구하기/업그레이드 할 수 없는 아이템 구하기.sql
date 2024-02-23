-- 코드를 작성해주세요
# not in 구문에서 원하는 결과를 보기 위해서는 다음과 같이 null을 제외하는 조건을 추가
select item_id, item_name, rarity
from ITEM_INFO
where item_id not in (select parent_item_id from item_tree where parent_item_id is not null)
order by item_id desc
