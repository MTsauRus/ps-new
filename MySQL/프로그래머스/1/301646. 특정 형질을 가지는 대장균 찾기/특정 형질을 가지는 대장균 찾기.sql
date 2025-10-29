select count(id) as count
from ecoli_data
where genotype & 2 = 0 and genotype & 5 in (1, 4, 5)