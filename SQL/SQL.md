* https://www.techbeamers.com/sql-query-questions-answers-for-practice/

<img src="http://www.mysqltutorial.org/wp-content/uploads/2019/10/MySQL-HAVING-Evaluation-Order.png" </img>

* https://artoftesting.com/sql-queries-for-interview
* https://www.c-sharpcorner.com/article/most-asked-sql-queries-in-interview-questions/


#### Installation & Configuration
~~~
* Mysql-server
* Workbench

$ sudo mysql -u root # I had to use "sudo" since is new installation

mysql> USE mysql;
mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY '';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;

$ service mysql restart

# For snap installation
$sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service

* https://www.geeksforgeeks.org/introduction-of-b-tree-2/

~~~

* [window functions 1](https://learnsql.com/blog/sql-window-functions-examples/)
* [window functions 2](https://towardsdatascience.com/intro-to-window-functions-in-sql-23ecdc7c1ceb)
* [window functions 3](https://learnsql.com/blog/sql-window-functions-examples/)
* [sqlserver window](https://www.sqlservertutorial.net/sql-server-window-functions/)
* [ Pivot Function ](https://codingsight.com/pivot-tables-in-mysql/)
* https://www.w3resource.com/mysql/mysql-functions-and-operators.php


### Practice Problems
* [Link](https://www.interviewbit.com/sql-interview-questions/)
* [Link]( https://www.techbeamers.com/sql-query-questions-answers-for-practice/)

#### Joins
* [ Different Join Types](https://miro.medium.com/max/966/0*Mu_d-mJMmaVX-j0P)

#### POSTGRES [Link](https://media.licdn.com/dms/image/v2/D4D22AQF8-yw6fRXhkw/feedshare-shrink_800/feedshare-shrink_800/0/1727379958393?e=1730332800&v=beta&t=1HL65EQbRzfaz9r5kUAUG9FJCTC0zMvQIYURGZO2v3o)

