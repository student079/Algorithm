-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where GENDER = 'W' and month(DATE_OF_BIRTH) = 3 and not isnull(TLNO)
order by MEMBER_ID