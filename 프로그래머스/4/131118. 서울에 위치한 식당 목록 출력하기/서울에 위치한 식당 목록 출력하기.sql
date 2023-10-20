-- 코드를 입력하세요
# 결과는 평균점수를 기준으로 내림차순 정렬
# 균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬
SELECT 
i.rest_id as REST_ID,
 i.rest_name as REST_NAME
 , i.food_type as FOOD_TYPE
 , i.favorites as FAVORITES
 , i.address as ADDRESS
 , round(avg(r.review_score),2) as SCORE
from rest_info as i join rest_review as r
on i.rest_id = r.rest_id
group by i.rest_id
having i.address like '서울%'
order by SCORE desc, FAVORITES desc