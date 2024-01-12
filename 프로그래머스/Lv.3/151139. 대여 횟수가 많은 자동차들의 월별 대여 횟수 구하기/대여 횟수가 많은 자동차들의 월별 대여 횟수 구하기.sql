-- 코드를 입력하세요
select month(START_DATE) as MONTH, CAR_ID, count(HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in 
(SELECT CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(start_date, "%Y-%m") between '2022-08' and '2022-10'
group by CAR_ID
having count(HISTORY_ID) >= 5)
and date_format(start_date, "%Y-%m") between '2022-08' and '2022-10'
group by MONTH, CAR_ID
having not RECORDS = 0
order by MONTH, CAR_ID desc