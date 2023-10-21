select food_type as FOOD_TYPE, rest_id as REST_ID, rest_name as REST_NAME, favorites as FAVORITES from rest_info
where (FOOD_TYPE, FAVORITES) in (select FOOD_TYPE, max(FAVORITES) from rest_info group by FOOD_TYPE)
order by FOOD_TYPE desc