-- Purpose of this project : explore dataset and find meaningful data to visualization.

-- Average loan by age 
select
	case
		when Age between 21 and 30 then '21-30'
        when Age between 31 and 40 then '31-40'
        when Age between 41 and 50 then '41-50'
        when Age between 51 and 60 then '51-60'
        else '61+'
	end as Age_group,
    avg(Loan) as Average_loan
from loan
group by Age_group;

-- Average loan by occupation
select Occupation, avg(loan) as Occupation_loan
from loan
group by Occupation
order by Occupation_loan desc;

-- Aveerage loan by gender
select Gender, avg(loan) as Gender_loan
from loan
group by Gender;

-- Average loan by income 
select
	case
		when Income < 30000 then 'Low'
        when Income >= 30000 and Income < 60000 then 'Midium'
        else 'High'
	end as Income_group,
    avg(loan) as Income_loan
from loan
group by Income_group;

-- Overdue list by occpation
select Occupation, avg(Overdue) as Occupation_overdue
from loan
group by Occupation
order by Occupation_overdue desc;