-- 코드를 작성해주세요
select ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPERS
where SKILL_CODE&(select sum(CODE) from SKILLCODES where NAME in('Python','C#'))
order by ID