with summation as (
    select flavor, sum(total_order) as tot
    from (
        select * from first_half
        union all
        select * from july
    ) as u
    group by flavor
    order by tot desc
)

select flavor from summation limit 3;