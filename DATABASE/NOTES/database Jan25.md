# Jan 25: Database Systems (Ch1, but like- half of it) #

**What is a Database System?**
    - Every Aspect of a Database-Involved Program's Function
    - [RDBMS] -> Relational Database Management Systems
    *Meta-Data:*
        - The Literal Data being Stored 
            - Important for the [Stored_Database_Definition]
            - Involved in the   [Information_Schema]
    **DBMS Software** 
        - Processes Queries to Access Stored Data 
        *DBMS Components*
            - Two Sides: [Data_Compilers] and [Transaction_Processing]
        **Transaction Processing**
            *Rollback*
                - Checks for consistency in some amount of past frames
        **Users/Compilers**
            *DDL - Data Definition Language*
                - Develops a Dictionary to Front-End Data Cataloging
            *Casual Users*
                - Shouldn't be able to do anything Too Crazy
                - [SQL-Injection]
                    - `select * from Account` -> takes Everything

**A Physical Centralized Architecture**
    *Time-Sharing Operating System*
        - Splits attention between two different Functions
        - Use Case Ex1: Two Users using the Database at Once
        - [Package-Switching]
            - Putting similar-purposed operations next to eachother

**How does Data Storage even work!?**
    *Storage Methods*
        - [Registers]
            - Parallel-Connected Lines of Stored Code 
            - These make adding/moving/removing easier
            - Goes at CPU Speed
        - [Cache]
            - Preserves Recently-Used Methods for Concision
            - Goes at Double-CPU Speed, Probably
        - [Memory]
            - Like, RAM n' Shit (Currently-Used Operations)
            - [Context_Switching]
                - Set-Aside Time to make sure Data is Properly Stored

**Client/Server Architecture**
    - Streamlines User/Server Engagement 
    - Provides 'Hubs' that can take/give Queries/Reponses to Users
    - [Oracle_7]
        - Introduced the [Multi-Thread_Server] (self-explanatory)