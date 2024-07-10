# 2021년 가입
# 상품을 구매한 회원 수
# 나누기 전체 회원수
#년, 월 별 출력
# 소수점 두번째자리에서 반올림
# 년월로 오름차순

with us as (
    select *
    from user_info
    where year(joined) = 2021
)

SELECT year(o.sales_date) as YEAR, month(o.sales_date) as MONTH,
count(distinct o.user_id) as PURCHASED_USERS,
round(count(distinct o.user_id) / (select count(*) from us), 1) as PURCHASED_RATIO
from us as u
join online_sale as o
on u.user_id = o.user_id
group by year(o.sales_date), month(o.sales_date)
order by YEAR, MONTH