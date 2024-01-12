-- 코드를 입력하세요
SELECT outs.ANIMAL_ID, outs.NAME
from ANIMAL_INS as ins right outer join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
where isnull(ins.ANIMAL_ID)
order by outs.ANIMAL_ID