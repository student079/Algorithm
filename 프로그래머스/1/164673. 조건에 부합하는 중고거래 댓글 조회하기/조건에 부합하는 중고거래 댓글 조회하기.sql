-- 코드를 입력하세요
SELECT b.title as TITLE, b.board_id as BOARD_ID, r.REPLY_ID as REPLY_ID, r.WRITER_ID as WRITER_ID,
 r.contents as CONTENTS, date_format(r.created_date,'%Y-%m-%d') as CREATED_DATE
from used_goods_board as b join used_goods_reply as r
on b.board_id = r.board_id
where year(b.created_date) = 2022 and month(b.created_date) = 10
order by CREATED_DATE asc, TITLE asc