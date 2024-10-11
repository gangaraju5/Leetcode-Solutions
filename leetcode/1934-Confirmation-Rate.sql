# Write your MySQL query statement below
select s.user_id, case when c.time_stamp is null THEN 0.00
else round(sum(c.action="confirmed")/count(*),2)
END as confirmation_rate
from signups as s
left join confirmations as c on s.user_id =c.user_id
group by s.user_id

