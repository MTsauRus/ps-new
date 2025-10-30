select a.id, b.fish_name, a.length
from fish_info as a
join fish_name_info as b
on a.fish_type = b.fish_type
join (
    select fish_type, max(length) as max_len
    from fish_info
    group by fish_type
    ) as t
    on a.fish_type = t.fish_type
    and a.length = t.max_len
order by a.id
;