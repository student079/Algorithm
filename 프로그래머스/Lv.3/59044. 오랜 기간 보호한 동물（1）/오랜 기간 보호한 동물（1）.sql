-- 코드를 입력하세요
SELECT ins.NAME, ins.DATETIME
from ANIMAL_INS as ins left outer join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
where isnull(outs.ANIMAL_ID)
order by ins.DATETIME
limit 3