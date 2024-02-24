-- 코드를 입력하세요
SELECT count(user_id) as USERS
from user_info
where joined like '2021%' and AGE <= 29 and AGE >= 20