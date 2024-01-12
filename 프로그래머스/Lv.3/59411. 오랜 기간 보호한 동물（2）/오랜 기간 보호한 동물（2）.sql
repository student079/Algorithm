-- 코드를 입력하세요
SELECT ins.ANIMAL_ID, ins.NAME
from ANIMAL_INS as ins join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
order by outs.DATETIME - ins.DATETIME desc
limit 2