-- 코드를 입력하세요
SELECT CART_ID
from CART_PRODUCTS 
where CART_ID in
(select CART_ID
from CART_PRODUCTS
where NAME = 'Milk')
and NAME = 'Yogurt'
order by ID