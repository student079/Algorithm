-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.PRICE * off.SALES_AMOUNT) as SALES
from PRODUCT as p join OFFLINE_SALE as off
on p.PRODUCT_ID = off.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE