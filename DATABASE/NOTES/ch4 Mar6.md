# March 6.th Database Notes #  
  
## CH.4 Relational Algebra ##  
  
### Language Heirarchy:  
**Language Levels:**  
    2. Function / Assembly (add, sub, etc-)  
    1. OpCode (Bits n Shit)  
    3. Procedural (Java, C++)  
    4. Fluent (SQL)  
  
### Relational Algebra:  
**METHODS:**  
    SELECT  : `σ <condition>      (R)` (σ Major ='CPSC')    
    PROJECT : `π <attribute list> (R)` (π Name, SSN, Major (STUDENT) )   
    RENAME  : `ρ (B1, B2, ...Bn)  (R)` (ρ STUDENT S1)   
    DIVISION: `R / S -> Attributes R that Match S` (ENROLL / ClassList)  
  
**SET OPERATIONS:**  
    UNION            : ------>  `adds Rows of BOTH, Columns ∪ Columns`  
    CARTESIAN PRODUCT: `R x S => adds Columns of BOTH, Rows * Rows`    
    INTERSECTION     : `looks for EXACT DATA MATCHES`  
    SET DIFFERENCE   : `removes INTERSECTING ELEMENTS from BOTH`  
  
**COMPLEX METHODS:**  
    JOIN    : `θ <condition> (S) = σ <condition> (R x S)`  
        {ex : θ <STUDENT.SSN=ENROLL.SSN>[ENROLL] = [STUDENT]*[ENROLL]  
  
### Summary of Relational Algebra:  
 **Aggregate Operations:**
    - represented with the french "F" 
        {ex : `<grouping attribute> F <func. list> (R)`}