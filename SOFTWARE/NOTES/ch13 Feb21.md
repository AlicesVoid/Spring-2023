# Feb 21.st SOFTWARE Notes #  
  
## ARCHITECTURAL DESIGN ##   
  
### Why Architecture? ###  
 **1. Analyze Design Effectiveness**  
 **2. Consider Architectural Alternatives**  
 **3. Reduce Risks of Structure**   
  
### Architecture Importance ###  
 **1. Representations Enable Fluid Communication**  
 **2. Architecture Highlights Design Decisions**  
 **3. "Constitutes a Relatively Small, Graspable Mode of System Op.**  
  
### Architectural Decisions ###  
 **IEEE Computer Society Definitions**  
    *Architectural Description (AD)*  
        "collective of products to doc. an architecture"  
    
### Architectural Genres ###  
 **Genre**   
    implies `Category` that defines `Software Domain`  
    [NOTE:] there are `Sub-Genres` (like Sub-Categories)  
  
### Architectural Styles ###  
 **Style Encompasses:**  
    `1. Set of Components`  
    `2. Set of Connectors`  
    `3. Constraints`  
    `4. Semantic Models`  
 **Style Types**  
    `Data-Centered   Architectures`  
        - Large [Data_Store] Sharing with [Client_Software]s  
    `Data Flow       Architectures`
        - [Pipes_and_Filters] Diagram  
        - [Batch_Sequential]  Diagram  
    `Call and Return Architectures`  
    `Object-Oriented Architectures`  
    `Layered         Architectures`  
        - [Layers_of_Access] (Think like Private/Protected/Public)    
    
### Architectural Patterns ###  
 **Concurrency**  
    - Repeat Tasks in a Parallel and Managed Pattern  
 **Persistence**  
    - DBMS and Application-Level Persistence  
 **Distribution**  
    - System-Environment Communication, i.e. Broker Component      
 **etc...**  
     
### Architectural Design ###     
 **Software must be placed in Context**   
    - Design details external factors and Nature of Interaction   
 **CONTEXT**   
    - You can freely add text to clarify roles in Diagrams   
 **Analysis**   
    *Method*   
        1. Collect Scenarios   
        2. Ellicit Req.s / Constraints / Environment Description   
        3. Describe the Architectural Styles/Patterns Chosen    
            a. Module / Process / Data-Flow View (Req. Model)   
        4. Evaluate Quality Attributes (select in Isolation)   
        5. Identify Quality Attribute Sensitivities per Arch. Styles  
        6. Critique Candidate Architectures using Step 5.   
   
### Architectural Complexity ###   
 **Consider the Dependencies between Components:**   
    1. Sharing     Dependencies   
    2. Flow        Dependencies    
    3. Constrained Dependencies (isolated user data)   
   
### Architectural Description Language (ADL) ###   
 **Provides Semantics & Syntax for Software Architecture**   
    - Represents Components/Blocks/Interfaces   
 **Partitioning**   
    - Data Diagrams can be Separated into Segments for Clarity   
    *Horizontal*   
        - Denotes Functions (does x-things, does y-things, etc...)   
    *Vertical*  
        - Denotes Factors (decision makers at top, workers at bottom)
       
### Structured Design ###   
 **Objective**
    - derive Partitioned Program Architecture
 **Approach**
    - a DFD mapped to Program Architecture
    - PSPEC and STD are used to indicate Module Content
 **Notation**
    - Structure Chart

### General Mapping ###  
 **1. Isolate Transform Center by Specifying Boundaries (Domain)**  
 **2. Perform "First-Level Factoring"**   
    - leads to a top-down map of program architecture
 **3. Perform "Second-Level Factoring**
    *Transform Map*
        - Produces an `Architecture` from a `Data Model` (pg 29)