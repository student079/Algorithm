-- 코드를 입력하세요
SELECT CAR_TYPE, count(car_type) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%가죽시트%'
group by CAR_TYPE
order by CAR_TYPE