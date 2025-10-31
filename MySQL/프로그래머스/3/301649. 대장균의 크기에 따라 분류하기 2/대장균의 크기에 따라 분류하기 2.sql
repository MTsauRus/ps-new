select id, 
     case ntile(4) over (order by size_of_colony desc)
            when 1 then upper('critical')
            when 2 then upper('high')
            when 3 then upper('medium')
            when 4 then upper('low')
            end as colony_name
from ecoli_data
order by id