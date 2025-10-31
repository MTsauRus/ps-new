with tmp as (
    select food_type, max(favorites) as max_favo
    from rest_info
    group by food_type
)

select a.food_type, a.rest_id, a.rest_name, t.max_favo as favorites
from rest_info as a
join tmp as t
on a.food_type = t.food_type and a.favorites = t.max_favo
order by a.food_type desc
;
