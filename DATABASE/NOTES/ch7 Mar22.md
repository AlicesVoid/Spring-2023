# March 22.nd Database Notes #    
  
## CH.7 MYSQL INTRODUCTION ##    
      
### MYSQL  
 **Connecting:**  
    `-mysql [-h host] [-u user] [-p[password]] [dbname]`  
 **Data Definitions:**  
     - `SHOW DATABASES;`  
     - `USE dbname;`  
     - `CREATE TABLE table_name(field_name type,..., constraints,...);`  
     - `SHOW TABLES;`  
     - `SHOW COLUMNS FROM table_name;`  
     - `DROP TABLE table_name;`  
 **Data Manipulation:**  
     - `INSERT INTO table_name[(field_name,...)] VALUES (value,...);`  
     - `DELETE FROM table_name[(field_name,...)] WHERE condition;`  
     - `UPDATE table_name SET field_name=value,...[WHERE condition];`  
     - `SELECT field_name [as field_name],...`    
          - `...FROM table_name [WHERE condition] [ORDER BY field_name];`  
     *NOTE:*  
          - `=, <, >, AND, OR, NOT (field_name LIKE "_%...")`  
 **Altering Tables:**   
     - `ALTER TABLE table_name...`  
          - `[RENAME new_table_name]`  
          - `[ADD field_name type]`  
          - `[DROP field_name]`  
          - `[CHANGE name new_name new_type];`  