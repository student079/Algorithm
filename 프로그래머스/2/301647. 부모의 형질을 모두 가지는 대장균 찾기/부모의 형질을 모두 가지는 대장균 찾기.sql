select a.id as ID, a.genotype as GENOTYPE, b.genotype as PARENT_GENOTYPE
from ecoli_data as a
join ecoli_data as b
on a.parent_id = b.id and b.genotype & a.genotype = b.genotype
order by a.id