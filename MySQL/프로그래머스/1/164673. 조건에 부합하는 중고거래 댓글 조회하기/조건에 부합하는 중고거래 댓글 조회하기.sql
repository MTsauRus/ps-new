select distinct
    B.title, 
    B.board_id,
    R.reply_id,
    R.writer_id,
    R.contents,
    date_format(R.created_date, '%Y-%m-%d') as created_date
from used_goods_board, used_goods_reply as R
join used_goods_board as B on B.board_id = R.board_id
where B.created_date like '2022-10%'
order by R.created_date, B.title;