-- 코드를 입력하세요
SELECT ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME
from ANIMAL_INS as ins join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
where ins.SEX_UPON_INTAKE like 'Intact%' 
and (outs.SEX_UPON_OUTCOME like 'Spayed%' or outs.SEX_UPON_OUTCOME like 'Neutered%')
order by ins.ANIMAL_ID