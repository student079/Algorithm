-- 코드를 입력하세요
SELECT BOOK_ID, date_format(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE from book
where PUBLISHED_DATE >= '2021-01-01' and PUBLISHED_DATE <= '2021-12-31' and category = '인문'
order by published_date asc