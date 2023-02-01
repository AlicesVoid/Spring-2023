# Jan 30th Database Notes #

## END OF CHAPTER 1: ##

**The Heirarchichal Model**
    - Details streamlined process breaking down user access to database entries 
    - Looks like a 3-Deep Tree that shows data relations
    - [PROBLEM]: Can't reverse-edit/check without difficulty
    *Surface-Level Depth*
        - Users (Customers, Departments, Suppliers)
    *First-Level Depth*
        - Methods (EMPS_MGR_Items, Orders) 
    *Lowest-Level Depth* 
        - Server Utilities (Entries, Offers)

**The Network Model**
    - Details data into related groups to streamline specific access
    - Allows more fluid editing of database values 
    - [PROBLEM]: Difficult to introduce new data / change query
        - you have to MOVE DATA AROUND 
    *Top-Level*
        - Items  
    *Middle-Level*
        - Function { LINKED RECORD OF DATA }
    *Bottom-Level*
        - Users   

**The Relational Model**
    - Details information in a data table that shows relationships
    *Top Row*
        - Data Titles
    *One Specific Column*
        - Proves relationship between different databases
    *Rest of it*
        - Tables indicating specific instance variables
    
## LECTURE 2 STARTS HERE ##

**The Entity-Relationship Model**
    [Entity]
        - a "thing" in the real world with an independent existence
        - has unique identity, has own properties 
    [Attributes]
        the properties that describe an entity:
        - can be [Composite] or [Simple] (can/cannot be sub-parted)
        - can be made of one or more Values
        - can be [Stored], or [Derived] from other attributes
        - can be made irrelevant or unknown ([NULL])
        - can be [Complex]: (includes [Composite] and [Multi-Var.])
        - can be [Key-Attributes]: (unique per entity)
        - has a  [Domain]: (all valid values that can be assigned)
    *(an) Entity Type:*
        - defines a Set of Entities that have the same Attributes
        - analagous to `Template` Classes in OOP
    *(an) Relationship Type:*
        - defines a Set of Associations among the same Entities
        - [Degree]: the number of participating Entity Types it has
        - [Cardinality_Ratio]: ratio showing the # of possible participants for a Relationship Type
        - [Participation_Constraints]: partial vs. toatl participation
    *Attributes of a Relationship Type:*
        - Some attributes cannot be moved to any single Entity Type 
        - They are better suited as attributes of Relationship Types
            - ex: "Hours->WorkOn" or "Grade->Semester"
         

