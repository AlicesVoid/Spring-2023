# Feb. 7th #

## Ch.11: Requirements Modeling

**Requirements Analysis**
    - specifies software's operational characteristics
    - indicates softwae's interface & backend elements
    - establishes constraints that software must meet 
    *Greater Purpose:*
        - elaborate on basic requirements 
        - build models to depict relationships / user-scenarios
    [RULES:]
        1. Model should focus on Visible Requirements (abstract it)
        2. Elements add insight to overall software requirements 
        3. Delay non-functional models up until design 
        4. Minimize coupling throughout system
        5. Be certain that the model is valuable to all stakeholders
        5. Keep it as simple as possible
    *Domain Analysis Method:*
        1. Define the domain to be investigated
        2. Collect representative sample of domain applications
        3. Analyze each application in the sample 
        4. Develop an analysis model for the objects
    [ELEMENTS:]
        - `Scenario-Based Models` (use-cases, user stories)
        - `Class Models`          (class diagrams, collab. diagrams)
        - `Behavioral Models`     (state diagrams, sequence diagrams)
        - `Flow Models `          (DFDs, Data Models, etc-)
    *Diagram References:*
        - Activity Diagram  (`ch.11 pg.13,15`)
        - Use-Case Diagram  (`ch.11 pg.14-15`)
        - Swimlane Diagrams (`ch.11 pg.16`)

**Data Modeling**
    - Examines `Data Objects` independently of Processing 
    - Focuses on `Data Domain`
    - creates a model at customer-level abstraction
    - indicates how data objects relate to one-another
    *Data Object:*
        - Representation of almost any Composite Info for Software
    *Relationships*
        - Objects are related through a variety of clarifiers 
            ex: person:car -> owns(), insured_to_drive(), etc...-

**The E-R Model, Again!** 
    - Legend: 
        - `Infinitely Many` | [Dot] [On-Line]
        - `Only One`        | [Double-Dash] [On-Line]
    - [UML_EXAMPLE:] `ch.11 pg.24`
    *The ERD:*
        -Levels:
            `Level 1.` - all Entities (data obj.) and their Connection
            `Level 2.` - all Entities, all Relationships
            `Level 3.` - Entities, Relationships, ETC-Attributes 
        NOTE:
            Level 3 is basically just a UML at that point
        [EXAMPLE:] `ch.11 pg.23`

**Class-Based Modeling**
    - Represents [obj.s], [operations], [relationships], and [collabs]
    *Identify Analysis Classes:*
        - Examine usage scenarios from Requirements Model
        - Perform a `Grammatical Parse:`
            1. Classes determined by underlining noun/noun-phrase
                a. store these in a table of sorts
            2. Synonyms should be noted
            3. if class(noun) is necssary, then: Solution Space
                a. if not, then: Problem Space 
    *Class-Responsibility-Collaborator (CRC) Model*
        Source: `ch.11 pg.32`
