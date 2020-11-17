CREATE DATABASE IF NOT EXISTS ORG;

CREATE TABLE Worker (
	WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FIRST_NAME CHAR(25),
	LAST_NAME CHAR(25),
	SALARY INT(15),
	JOINING_DATE DATETIME,
	DEPARTMENT CHAR(25)
);

INSERT INTO Worker 
	(WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
		(001, 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'HR'),
		(002, 'Niharika', 'Verma', 80000, '14-06-11 09.00.00', 'Admin'),
		(003, 'Vishal', 'Singhal', 300000, '14-02-20 09.00.00', 'HR'),
		(004, 'Amitabh', 'Singh', 500000, '14-02-20 09.00.00', 'Admin'),
		(005, 'Vivek', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin'),
		(006, 'Vipul', 'Diwan', 200000, '14-06-11 09.00.00', 'Account'),
		(007, 'Satish', 'Kumar', 75000, '14-01-20 09.00.00', 'Account'),
		(008, 'Geetika', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin');

CREATE TABLE Bonus (
	WORKER_REF_ID INT,
	BONUS_AMOUNT INT(10),
	BONUS_DATE DATETIME,
	FOREIGN KEY (WORKER_REF_ID)
		REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Bonus 
	(WORKER_REF_ID, BONUS_AMOUNT, BONUS_DATE) VALUES
		(001, 5000, '16-02-20'),
		(002, 3000, '16-06-11'),
		(003, 4000, '16-02-20'),
		(001, 4500, '16-02-20'),
		(002, 3500, '16-06-11');
        

CREATE TABLE Title (
	WORKER_REF_ID INT,
	WORKER_TITLE CHAR(25),
	AFFECTED_FROM DATETIME,
	FOREIGN KEY (WORKER_REF_ID)
		REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Title 
	(WORKER_REF_ID, WORKER_TITLE, AFFECTED_FROM) VALUES
 (001, 'Manager', '2016-02-20 00:00:00'),
 (002, 'Executive', '2016-06-11 00:00:00'),
 (008, 'Executive', '2016-06-11 00:00:00'),
 (005, 'Manager', '2016-06-11 00:00:00'),
 (004, 'Asst. Manager', '2016-06-11 00:00:00'),
 (007, 'Executive', '2016-06-11 00:00:00'),
 (006, 'Lead', '2016-06-11 00:00:00'),
 (003, 'Lead', '2016-06-11 00:00:00');
 
 # problems
 
# select first 3 charecters of worker
select substring(first_name,1,3) from Worker;
 
 #Q-5. Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
 select instr(first_name,binary'a') from Worker where first_name="Amitabh";
 
 #Q-6. Write an SQL query to print the FIRST_NAME from Worker table after removing white spaces from the right side.
 select Rtrim(first_name) from Worker;
 
 # Q-8. Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length.
 select distinct length(department) from Worker;
 
 #Q-9. Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.
 select replace(first_name,'a','A') from Worker;
 
 # Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them.
 select concat(first_name," ",last_name) as complete from Worker;
 
 #Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them.
 select * from Worker where first_name not in ("Vipul" ,"Satish");
 
 #Q-15. Write an SQL query to print details of Workers with DEPARTMENT name as “Admin”.
 select * from Worker where department 	="Admin%";
 
 #Q-20. Write an SQL query to print details of the Workers who have joined in Feb’2014.
 select * from Worker where year(JOINING_DATE)= 2014 and month(JOINING_DATE)>=2;
 
 #Q-22. Write an SQL query to fetch worker names with salaries >= 50000 and <= 100000.
 select CONCAT(FIRST_NAME, ' ', LAST_NAME) As Worker_Name, Salary from Worker where Salary BETWEEN 50000 AND 100000;
 
 SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) As Worker_Name, Salary
FROM worker 
WHERE WORKER_ID IN 
(SELECT WORKER_ID FROM worker 
WHERE Salary BETWEEN 50000 AND 100000);

#Q-23. Write an SQL query to fetch the no. of workers for each department in the descending order.
select count(*) from Worker group by department desc;

#Q-24. Write an SQL query to print details of the Workers who are also Managers.
select * from 
Worker  w
inner join Title  t
where w.worker_id=t.worker_ref_id and t.worker_title="manager";

# Q-25. Write an SQL query to fetch duplicate records having matching data in some fields of a table.
SELECT *
FROM Worker
where worker_id in
(select worker_id from Title
GROUP BY WORKER_ID
HAVING COUNT(*) > 1);

#Q-26. Write an SQL query to show only odd rows from a table.
set @i:=0;
select worker_id from 
(select @i := @i+1 as i,worker_id from Worker) a
where mod(a.i,2)=0;

#Q-28. Write an SQL query to clone a new table from another table.
create table w2 like  Worker;

#Q-29. Write an SQL query to fetch intersecting records of two tables.
#(SELECT * FROM Worker)
#INTERSECT oracle
#(SELECT * FROM w2);

#Q-31. Write an SQL query to show the current date and time.
select curdate();
select curtime();
select now();

# Q-33. Write an SQL query to determine the nth (say n=5) highest salary from a table.
SELECT Salary FROM Worker ORDER BY Salary DESC LIMIT 5,5;

#Q-35. Write an SQL query to fetch the list of employees with the same salary.
Select distinct W.WORKER_ID, W.FIRST_NAME, W.Salary 
from Worker W, Worker W1 
where W.Salary = W1.Salary 
and W.WORKER_ID != W1.WORKER_ID;

#Q-36. Write an SQL query to show the second highest salary from a table.
select * from Worker
order by salary desc
limit 2,1;

Select max(Salary) from Worker 
where Salary not in (Select max(Salary) from Worker);


#Q-39. Write an SQL query to fetch the first 50% records from a table.
set @i:=0;
SELECT a.i
FROM ( select @i:=@i+1 as i,Worker_id,first_name from Worker) a
WHERE a.i <= (select (count(*))*.3 from Worker);

#Q-40. Write an SQL query to fetch the departments that have less than five people in it.
select count(*),department from Worker group by department having count(*)<=2;

#Q-42. Write an SQL query to show the last record from a table.
select * from Worker
order by worker_id desc
limit 0,1;

Select * from Worker where WORKER_ID = (SELECT max(WORKER_ID) from Worker);

SELECT * FROM Worker WHERE WORKER_ID <=5
UNION
SELECT * FROM (SELECT * FROM Worker W order by W.WORKER_ID DESC) AS W1 WHERE W1.WORKER_ID <=5;

#Q-44. Write an SQL query to fetch the last five records from a table.
select * from (select * from Worker
order by worker_id desc
limit 0,5) t
order by t.worker_id asc;

#Q-45. Write an SQL query to print the name of employees having the highest salary in each department.
select department,max(salary) from Worker
group by department;

#with multiple highest salaries

select w.department,w.first_name,w.salary
from
(select department,max(salary) as salary from Worker
group by department)a
inner join Worker w
on a.department=w.department
and a.salary=w.salary;

#Q-46. Write an SQL query to fetch three max salaries from a table.

SELECT distinct Salary from Worker a WHERE 3 >= (SELECT count(distinct Salary) from Worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;

select  t.Salary from (select distinct(salary) as Salary from Worker) t
order by Salary desc
limit 0,3;


#Q-48. Write an SQL query to fetch 5th max salaries from a table.

select * from (select distinct(Salary)as Sal from Worker)t
order by t.sal desc
limit 4,1;

SELECT distinct Salary from Worker a WHERE 5 >= (SELECT count(distinct Salary) from Worker b WHERE a.Salary <= b.Salary) order by a.Salary desc;