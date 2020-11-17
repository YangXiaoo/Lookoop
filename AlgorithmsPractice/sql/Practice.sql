# 182
select Email from Person group by Email having count(Email) > 1;

# 595
select name, population, area 
from World
where area > 3000000 or population > 25000000;

# 620
select * 
from cinema 
where description != 'boring' and id % 2 = 1 
order by rating desc;

# 175
select p.FirstName, p.LastName, a.City, a.State
from Person p left join Address a
on p.PersonId = a.PersonId;

# 181
select  e1.Name
from Employee e1, Employee e2
where e1.ManagerId = e2.Id and e1.ManagerId != null and e1.Salary > e2.Salary;

# 183
select c.Name as Customers
from Customers c 
left join Orders o 
on c.Id = o.Id 
where o.CustomerId is null;

# 197
select w1.Id
from Weather w1, Weather w2
where DATEDIFF(w1.RecordDate, w2.RecordDate) = 1 and w1.Tmperature > w2.Tmperature;

# 列出超过或等于5名学生的课
select class
from Courses
group by class
having count(DISTINCT student) > 4;

# 176
# 第二高的薪水
select max(e.Salary) as SecondHighestSalary
from Employee e
where e.Salary < (select max(Salary) from Employee);

select Salary as SecondHighestSalary
from (select e1.*, rownum r from (select * from Employee order by Salary desc) e1 where r < 2) 
where r >= 1

# 626 换座位

# 178 分数排名
select s1.Score as score, count(distinct(s2.Score)) as `Rank`
from Scores s1, Scores s2
where s1.Score <= s2.Score 
group by s1.Id 
order by `Rank` asc;

# 180 连续出现三次的数字
select distinct l1.Num as ConsecutiveNums
from Logs l1, Logs l2, Logs l3
where l1.Num = l2.Num and l2.Num = l3.Num and l2.Id - l1.Id = 1 and l3.Id - l2.id = 1;

# 184 部门工资最高的员工
select d.Name as Department, e.Name as Employee, e.Salary
from Employee e inner join Department d
on e.DepartmentId = d.Id and e.Salary >= (select max(Salary) from Employee where d.Id = DepartmentId);

select o1.Name as Department, e2.Name as Employee, e2.Salary
from Employee e2
left join
    (select distinct e.DepartmentId eId, max(e.Salary) highSalary, d.Name Name
    from Employee e left join Department d on e.DepartmentId = d.Id
    group by e.DepartmentId) o1
on o1.eId = e2.DepartmentId
where e2.Salary = o1.highSalary and o1.Name is not null;