-- 코드를 작성해주세요
select item_tree.item_id, item_info.item_name, item_info.rarity from item_info join item_tree 
on item_info.item_id = item_tree.item_id
where item_tree.parent_item_id in (select item_id from item_info
where rarity = 'RARE')
order by item_tree.item_id desc