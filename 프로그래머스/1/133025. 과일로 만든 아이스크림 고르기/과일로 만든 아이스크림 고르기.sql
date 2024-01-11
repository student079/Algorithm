-- 코드를 입력하세요
SELECT h.flavor
from first_half as h join icecream_info as i
on h.flavor = i.flavor
where h.TOTAL_ORDER > 3000 and i.INGREDIENT_TYPE = 'fruit_based'
order by h.TOTAL_ORDER desc