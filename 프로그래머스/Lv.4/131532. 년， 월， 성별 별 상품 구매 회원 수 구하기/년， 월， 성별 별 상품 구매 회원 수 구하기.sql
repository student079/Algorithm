-- 코드를 입력하세요
SELECT year(s.sales_date) as YEAR, month(s.sales_date) as MONTH, u.GENDER as GENDER,
count(distinct(u.USER_ID)) as USERS
from USER_INFO as u join ONLINE_SALE as s
on u.USER_ID = s.USER_ID
where not isnull(u.GENDER)
group by year(s.sales_date), month(s.sales_date), u.GENDER
order by YEAR, MONTH, GENDER