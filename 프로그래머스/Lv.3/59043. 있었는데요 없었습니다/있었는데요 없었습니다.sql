-- 코드를 입력하세요
SELECT ins.ANIMAL_ID, ins.NAME
from ANIMAL_INS as ins join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
where outs.DATETIME < ins.DATETIME
order by ins.DATETIME