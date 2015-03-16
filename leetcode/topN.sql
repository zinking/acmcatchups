select 
  e.Salary, 
  count(distinct(t.Salary)) as rank
from
  Employee e
  join
  Employee t
  on 
      t.Salary >= e.Salary
