with rental_month as (
    select month(start_date) as month, car_id, count(*) as tot
    from car_rental_company_rental_history
    where start_date between '2022-08-01' and '2022-10-31'
    group by car_id, month
    having tot > 0
)

select a.month, a.car_id, a.tot as records
from rental_month as a
where a.car_id in (
    select car_id
    from car_rental_company_rental_history
    where start_date between '2022-08-01' and '2022-10-31'
    group by car_id
    having count(*) >= 5
)
order by a.month, car_id desc;