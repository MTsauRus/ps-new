with month_fee as (
select car_type, discount_rate from car_rental_company_discount_plan
where duration_type like '%30%')

select distinct a.car_id, a.car_type, round((a.daily_fee * 30 * (100 - c.discount_rate) * 0.01), 0) as fee
from car_rental_company_car as a
join car_rental_company_rental_history as b
on a.car_id = b.car_id
join month_fee as c
on a.car_type = c.car_type
where a.car_type in ('세단', 'SUV') and a.car_id in (select car_id from car_rental_company_rental_history
                group by car_id
                having max(end_date) < '2022-11-01')
and
round((a.daily_fee * 30 * (100 - c.discount_rate) * 0.01), 0) >= 500000 and round((a.daily_fee * 30 * (100 - c.discount_rate) * 0.01), 0) < 2000000
order by fee desc, a.car_type asc, a.car_id desc;