# March 6.th Database Notes #  
  
## CH.5 Query Organization ##  
    
### Summary of Forming Queries  
 **Steps:**   
    1. find `the minimum set of schemas`:  
        a. find attrbiutes involved in conditions and results  
        b. find relation schemas that contain step 1 qualities  
        c. find other schemas that connect step 1 and step 1_a   
    2. Form the `Query`:  
        a. start with the most specific condition   
        b. if [Join] is necessary, `join two schemas` every time  
        c. project to the necessary attributes (keys/connections)  
        d. repeat steps 2_b and 2_c until all results are retrieved  
 **Basic Example:**  
    `Q1: Retrieve Names & Addresses of all Employess in Research Dept.`:  
    - relational solution:  
        1. `RD <- σ_DNAME = 'research'(DEPARTMENT)`  
        2. `Result`:   
            a. `<- π_FNAME,LNAME,ADDRESS(EMPLOYEE θ DNO=DNUMBER(RD))`  
    - SQL solution:  
        1. `SELECT FNAME, LNAME, ADDRESS`  
        2. `FROM EMPLOYEE, DEPARTMENT`   
        3. `WHERE DNAME ='research' AND DNUMBER = DNO;`  
  
### ADDITIONAL INFO (FROM BOOK NOT SLIDES):  
 **Additional Keywords:**  
    - LIKE: `<expr> LIKE <string>` | (%) -> Mult. 0s , (_) -> 1 char.  
    - ORDER BY: `ORDER BY <attribute list>` | DESC or ASC  
    - ALL: `<expr> ALL <schema(s)>`  
    - EXISTS: `<expr> EXISTS <schema(s)>`  
 **Tables as Sets in SQL:**  
    - either-or problems: `Union two Schema Sets` Together  
 **Suggestive Schema:**  
    - popular schema to find attributes lacking some connections
    - ex: { `<expr1_attribute1>(R) - <expr2_attribute1>(S)`}  
