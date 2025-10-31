select a.category, sum(b.sales) as total_sales
from book as a
join book_sales as b
on a.book_id = b.book_id
where b.sales_date between '2022-01-01' and '2022-01-31'
group by a.category
order by a.category;