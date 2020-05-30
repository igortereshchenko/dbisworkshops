insert into repeatedly
(monday, tuesday, wednesday, thursday, friday, saturday, sunday)
with cteFlags (Value)
AS
(
SELECT '0' AS Value
from dual
UNION ALL
SELECT '1'
from dual
)
SELECT
Flag0.Value,
Flag1.Value,
Flag2.Value,
Flag3.Value,
Flag4.Value,
Flag5.Value,
Flag6.Value
FROM cteFlags Flag0
CROSS JOIN cteFlags Flag1
CROSS JOIN cteFlags Flag2
CROSS JOIN cteFlags Flag3
CROSS JOIN cteFlags Flag4
CROSS JOIN cteFlags Flag5
CROSS JOIN cteFlags Flag6;



insert into time_dim (time, hour, minutes)
with cte_h (h)
as
(
select 0
from dual
union all
select h+1
from cte_h
where h<23
),
cte_m (m)
as
(
select 0
from dual
union all
select m+1
from cte_m
where m<59
)
select 
case 
    when h >= 10 and m >= 10
    then to_char(h) || ':' || to_char(m)
    when h >= 10 and m < 10
    then to_char(h) || ':' || '0' || to_char(m)
    when h < 10 and m >= 10
    then '0' || to_char(h) || ':' || to_char(m)
    else '0' || to_char(h) || ':' || '0' || to_char(m)
end time,
h,
m 
from cte_h, cte_m
order by h, m
;