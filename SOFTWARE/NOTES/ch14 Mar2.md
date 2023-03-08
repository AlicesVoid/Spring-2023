# March 2.nd Software Notes #   
  
## Chapter 14 Part 2: MORE COMPONENTS!!!  
  
### Reuse   
 **Component-Based Development**  
    - Reuse is very helpful in saving time  
 **Impediments**
    - Reuse is difficult to plan ahead for 
    - Companies may not incentivise writing Reusable Code  
  
### CBSE  
 **The CBSE Process:**  
    - `Domain Engineering` Dictates `Software Engineering`  
    - Components should be Standardized in a Library 
 **Domain Engineering**  
    1. Define the Domain to Investigate   
    2. Categorize the Items in the Domain   
    3. Collect a sample of Applications in the Domain   
    4. Analyze each Sample Application  
    5. Develop an Analysis Model for the Objects  
 **Identify Reusable Components**  
    - Literally just Identify Code Patterns and Go From There  
 **CBSE Activities:**  
    - `Component Qualification`  
        - Consider if it is Secure/Flexible/Reliable Enough  
    - `Component Adaptation`  
        - Simple Design with Common Data Management Methods  
    - `Component Composition`  
        - Infrastructure is Necessary to achieve Common Goals  
    - `Component Update`  

### OMG / CORBA
 **Common Object Request Broker Architecture (COBRA):**
    - `Object Request Broker (ORB)` provides Component Communication  
    - `Interface Definition Language (IDL)` defines Component Systems  
    - `Objects` within a Client App request ORB Components  
    - `Requests` are made with an IDL or Dynamically at Run Time  
 **Examples:**  
    - `Microsoft COM` -> Adjusts Windows per Computer Components   
    - `Sun JavaBeans` -> Lets you write Custom Java Components  
  
### Component Classifications  
 **Enumerated Classification:**  
    - Components are described with Heirarchy and Subclasses  
 **Faceted Classification:**  
    - Domain Area is Analzyed to Identify Basic Descriptive Features  
 **Attribute-Value Classification**  
    - A Set of Attributes is Defined for All Components in Domain  
  
### Reusability Environments 
 **The Reuse Environment:**  
    - A Component Database capable of Storing / Retrieving Components
 **Examples:**  
    - Node Packet Manager (npm)  
    - Package Installer for Python (pip)  
    - Unity Package Manager / Unreal Marketplace
