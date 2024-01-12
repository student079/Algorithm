-- 코드를 입력하세요
select m.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW as r join MEMBER_PROFILE as m
on m.MEMBER_ID = r.MEMBER_ID
where m.MEMBER_ID = 
(SELECT m.MEMBER_ID
from MEMBER_PROFILE as m join REST_REVIEW as r
on m.MEMBER_ID = r.MEMBER_ID
group by m.MEMBER_ID
order by count(REVIEW_ID) desc
limit 1)
order by REVIEW_DATE, r.REVIEW_TEXT