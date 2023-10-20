-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH,'%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where month(date_of_birth) = 3 and not tlno is null and gender = 'W'
order by member_id asc