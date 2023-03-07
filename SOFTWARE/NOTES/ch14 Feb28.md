# Februrary 28.th Software Notes #    
  
## Chapter 14: Component-Level Design   
  
### Components  
 **What are they?**  
    - Some Connected Logical Objects that have Problem-Solving App.s  
 **Basic Design Principles:**   
    `1. Open-Closed Principle (OCP)`  
        - open for extension, closed for modification  
    `2. Liskov Substitution Prinsiple (LSP)`      
        - subclasses should be subsitutible for base classes  
    `3. Dependency Inversion Principle (DIP)`  
        - depends on abstractions, not on concretions (flex)  
    `4. Interface Segregation Principle (ISP)`  
        - multiple interfaces is better than one multi-purpose one  
    `5. Rlease Reuse Equivalency Principle (REP)`  
        - "the granule of reuse is the granule of release"  
    `6. Common Closure Principle (CCP)`  
        - "classes that change together, belong together"  
    `7. Common Reuse Principle (CRP)`  
        - "classes that dont change together, dont belong together"   
  
 **Syntax Design Guidelines**  
    `1. Components:`  
        - Define a Naming Convention for Architectural Components  
    `2. Interfaces:`  
        - Determines Collaborating Classes Easily (does OPC too)  
    `3. Dependencies and Inheritance`  
        - Dependencies -> Left to Right, Inheritance -> Bottom to Top  
          
### Structure Chart  
 **Legend:**  
    - White Nodes | `Control Components` (manager/sender/etc-)  
    - Blue  Nodes | `Problem Domain Components` (solution(task))  
  
### Component Concepts  
 **Cohesion**  
    - the "single-mindedness" of a module  
    *Layers of Cohesion:*  
        - Functional, Layer,  Communicational, Sequential,    
            - Procedural, Temporal, utility  
 **Coupling**  
    - the "multi-facetedness" of a module  
    *Layers of Coupling:*  
        - Content, Common, Control, Stamp, Data, Routine Call,   
            - Type use, Inclusion/Import, External  
  
### Component-Level Design  
 **NOTE:**  
    - the Processing Logic is governed by Basic Algo. Principles  
    - the Data Structures are defined by the Sys. Data Model(s)  
    - the Interface Design is governed by Collaborating Components  
 **STEPS:**  
    1. Identify Design Classes corresponding to Problem Domain  
    2. Identify Design Classes corresponding to Infrastructure Domain  
    3. Elaborate Design Classes that are not Reusable  
        3a. Specify Messages when Classes Communicate  
        3b. Identify Appropriate Interfaces for Components  
        3c. Elaborate Attributes and Define Data Types / Structures  
        3d. Describe Processing Flow for each Operation in Detail  
    4. Describe Persistent Data Sources and Identify Req.'d Classes  
    5. Develop and Elaborate Behavioral Representations of Classes  
    6. Elaborate Deployment Diagrams to Add Implementation Info  
    7. Factor every Component-Level Design; Consider Alternatives  
  
### Design for WebApps  
 **Components**  
    - `WebApp Components` incorporate Content & Functional Designs    
 **Contents**  
    - `WebApp Contents` often have Package Presentation Constraints  
 **Functions**  
    - `WebApp Functions` often mimic similar conventional components  
  
### Algorithm Design   
 **Algorithms**  
    - The Closest Design Activity to Actually Coding  
 **Algorithm Design Methods**    
    1. review the design description of the component  
    2. use `Stepwise Refinement` to develop algorithm  
    3. use Structured Programming to implement procedural logic  
    4. use 'format methods' to prove logic  
 **Stepwise Refinement:**  
    - Add detail to Steps Incrementally  
 **Algorithm Design Model**  
    - ANY procedural method to express the flow of behaviors.  
  
### Structured Programming  
 **Limited Set of Logical Constructs:**  
    - `Sequence`  
    - `Conditionals` (if-then-else, etc-)  
    - `Loops`  
    *Why do This?*  
        - Leads to more Readable and Testable Code   
        - works in-junction with 'proof of correctness'  
        - important for achieving high quality, but not enough  
 **Decision Table:**  
    - Maps `Assertions` to their respective `Predicates`  
 **Program Design Language (PDL)**  
    - aka Pseudocode   
    - write like you're almost-coding and you'll usually nail it  
    *Why do This?*  
        - what if the Designer is NOT the Coder?  
        - much easier to review than real code  
  
    