with tmp as (
    select
    id,
    fish_type,
    ifnull(length, 10) as length,
    time
    from fish_info
)

select count(id) as fish_count, max(length) as max_length, fish_type
from tmp
group by fish_type
having avg(length) >= 33
order by fish_type;