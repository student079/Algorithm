-- 코드를 입력하세요
SELECT ANIMAL_ID
from ANIMAL_INS
where not isnull(NAME)
order by ANIMAL_ID