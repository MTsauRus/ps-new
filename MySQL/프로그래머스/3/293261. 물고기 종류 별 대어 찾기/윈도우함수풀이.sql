with fish_rank as (
    select a.id, b.fish_name, a.length, 
        rank() over (
            partition by a.fish_type
            order by a.length desc
        ) as rnk
    from fish_info as a
    join fish_name_info as b
    on a.fish_type = b.fish_type)
    
select id, fish_name, length
from fish_rank
where rnk = 1
order by id;
