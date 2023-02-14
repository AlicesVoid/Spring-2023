# Feb 14th SOFTWARE notes!!! #

## Chapter 12: Design Concepts ##

**Good Software Design**
    1. `Firmness` - a program should not have any bugs, ideally
    2. `Commodity`- a program should be suitable for it's purpose
    3. `Delight`  - a program should be pleasurable to use

**Design and Quality**
    *Notable Design Features:*
        1. design must implement ALL explicit features
        2. design must be a readable, understandable guide
        3. design should provide a complete picture of the software
    *Quality Guidelines*
        1. design should exhibit an architecture that:
            a. has been created using recognizable patterns
            b. is composed of well-designed components
            c. can be implemented in an evolutionary fashion
        2. design should be modular
        3. design should contain distinct/holistic representations
        4. design should lead to appropriate data structures 
        5. design should use independent-functional components
        6. design should lead to simple interfaces
        7. design should be derived using a repeatable methodic errors
        8. design should be represented using effective notation
    *Design Principles*
        - avoid 'tunnel vision'
        - take inspiration from analysis model
        - don't 'reinvent the wheel'
        - design should "minimize intellectual distance" 
        - exhibit uniformity in integration
        - structure to accomodate change
        - structure to decay gently
        - design is not coding. coding is not design.
        - assess design for quality
        - review designs to minimize semantic errors
    *Fundamental Concepts*
        - `Abstraction`
        - `Architecture`
        - `Patterns`
        - `Separation of Concerns` concerns are REQUIRED problems
        - `Modularity`
        - `Hiding`
        - `Functional Independence`
        - `Refinement`
        - `Aspects`
        - `Refactoring`
        - `OO Design Concepts`
        - `Design Classes`
    *Data Abstraction*
        - traits of an object can be generalized using a noun and verb
            - simplifies things to make them easier to use!!!
        `Procedural Abstraction` -> Object is known for a Procedure
            (ex: door.open() simplifies the door attributes)
    *Patterns*
        - include: 
            Name, Synonyms, Intent
            Example of Pattern Instance
            Domain, Structure, Participants (responsiblities)
            Collaborations, Consequences, Related Patterns
    *Modularity*
        - There is a number of modules s.t. cost is minimized
        - sizing: 
            - what's inside? and 
            - how big is it?
    *Information Hiding*
        - designing client-side interfaces inside of classes 
            - this minimizes "side effects"
        `stepwise refinement` -> less hiding implies more detail
    *Functional Independence*
        - functions should be "single-minded" with "aversions":
        - `Cohesion` -> relative functional strength of a module
        - `Coupling` -> relative independence among some modules
    *Aspects*
        - representation of a `cross-cutting concern`:
            - concern that requires 2 concerns to be addressed at once
    *Refactoring*
        - process of changing a software system s.t. it flows better
            - i.e. code is the same but internal structure is new
        - [CONCERNS:]
            - Redundancy, Unused Elements, Inefficient Algo.s, etc...
    *OO Design Concepts*
        - `Design Classes` {entity, boundary, controller, etc-}
            [NOTE:]
                - Entity     -> Analysis Class
                - Boundary   -> Interface Class
                - Controller -> Management Class
        - `Inheritance`    {subclass inherits superclass' facets}
        - `Messages`       {stimulate some behavior in recieving obj.}
        - `Polymorphism`   {greatly reduces effort to extend design}
        **The Design Model**
            inspired from `Analysis Model` {ch.12 pg.24}
            *Elements:*
                `Data Elements`         {Data Structures/Databases}
                `Architectural Elements`{Requirements/Patterns/Domain}
                `Interface Elements`    {UI/External Access}
                `Component Elements` 
                `Deployment Elements`