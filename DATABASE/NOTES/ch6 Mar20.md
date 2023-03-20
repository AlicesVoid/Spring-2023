# March 20.th Database Notes #  
  
## CH.6 Query Organization ##  
    
### STRUCTURED QUERY LANGUAGE (SQL)   
    NOTE: see page 2 slide 2 for examples  
 **1. Create a Database:**    
    - `CREATE DATABASE <dbname>;`  
    - `GRANT ALL ON <dbname>.* TO <user>@localhost`  
        - `IDENTIFIED BY <password>`    
    
 **2. Create a Table:**   
    - `CREATE TABLE <tablename>`  
        - `(  <col> <datatype> [<attribute constraint>] `  
        - `{, <col> <datatype> [<attribute constraint>]}`  
        - `[ <table constraint> {, <table constraint>}] )`
  
 **3. Drop Table:**   
    - `DROP DATABASE <dbname>`    
    - `DROP TABLE <tablename>`  
    - `DROP PRIMARY (<col> {, <col>})`
    - `DROP UNIQUE  (<col> {, <col>})`  
    - `DROP CONSTRAINT <name>`    
  
 **4. Alter Table:**  
    - `ALTER TABLE <tname>`   
        - follow this with: ADD/MODIFY/RENAMETO/DROP/etc...     
    [NOTE:]  
        - `ADD    (<col> <datatype> {, <col> <datatype>})`  
        - `MODIFY (<col> <datatype> {, <col> <datatype>})`    
        - `RENAMETO <newname>`  
    
 **5. Insert Tuples:**   
    - `INSERT INTO <tname> VALUES(<val1>,...<valn>)`  
    - `INSERT INTO <tname>(<attr1>,...) VALUES (<val1>,...)`  
    [NOTE:]   
        - this adds the items in order that They were Created In  
   
 **6. Update table:**  
    - `UPDATE <tname> SET <attribute>=<val> WHERE <conditions>`  
   
 **7. Delete:**  
    - `DELETE FROM <tname> WHERE <conditions>`  
   
### SQL Datatypes    
 **Datatypes:**  
    1. `CHAR<size>                                | {< 255 bytes}`  
    2. `VARCHAR<size>                             | {< 255 bytes}`  
    3. `BLOB or TEXT                              | {< 65,535 bytes}`   
    4. `MEDIUMBLOB or MEDIUMTEXT                  | {< 16,177,215}` 
    5. `LONGBLOB or LONGTEXT                      | {< 4 Gigs}`     
    6. `ENUM(<val1>,...<valn>)                    | `    
    7. `TINYINT, SMALLINT, MEDIUMINT, INT, BIGINT | {1,2,3,4,8 bytes}`  
    8. `DECIMAL or NUMERIC(M, D)                  | {M, D}`  
    9. `FLOAT                                     | {4 bytes}`  
    10. `DOUBLE PRECISION                         | {8 bytes}`  
    11. `DATE(YYYY-MM-DD usually)                 |`  
  
 **Attribute Constraints:**   
    1. `NOT NULL`  
    2. `UNIQUE`  
    3. `PRIMARY KEY`  
    #. `DEFAULT <val>`
   
 **Table Constraints: [CONSTRAINT <name>]**  
    1. `PRIMARY KEY (<attribute> {, <attribute>})`  
    2. `FOREIGN KEY (<attribute> REFERENCES <table>(<attribute>)`  
        2a. `(also add this:) ON DELETE CASCADE | ON DELETE SET NULL`    
    3. `UNIQUE KEY (<attribute> {, <attribute>})`  
  
