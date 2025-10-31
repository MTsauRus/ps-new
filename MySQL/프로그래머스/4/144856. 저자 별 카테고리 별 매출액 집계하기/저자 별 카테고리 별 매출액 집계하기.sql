select a.author_id, b.author_name, a.category, sum(c.sales * a.price) as total_sales
from book as a
join author as b on a.author_id = b.author_id
join book_sales as c on a.book_id = c.book_id
where c.sales_date between '2022-01-01' and '2022-01-31'
group by a.category, a.author_id
order by a.author_id, a.category desc;