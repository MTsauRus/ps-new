select
    car_id, 
    case 
        when 
            sum(if('2022-10-16' between start_date and end_date, 1, 0)) = 0
            then '대여 가능'
        else '대여중'
    end as availability
from car_rental_company_rental_history
group by car_id
order by car_id desc;