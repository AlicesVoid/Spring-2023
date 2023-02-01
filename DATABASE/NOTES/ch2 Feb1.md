# Feb 1.st Chapter 2 Database Notes!!! #
    
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
    *Weak Entity Types*
        - Entity that is related to some Owner Entity
    
**E-R DIAGRAM SYMBOLIC LEGEND**
    `Entity`                        | [Rectangle]
        `Weak Entity`               - [Rectangle] [Bordered]
    `Relationship`                  | [Diamond]
        `Identifying Relationship`  - [Diamond] [Bordered]
    `Attribute`                     | [Ellipse]
        `Key Attribute`             - [Ellipse] [Underline]
            `Partial Key Attribute` | [Ellipse] [Dotted] [Underline]
        `Multivalued Attribute`     - [Ellipse] [Bordered]
        `Composite Attribute`       | [Ellipse] [Line]
        `Derived Attribute`         - [Ellipse] [Dotted]
    `Total Participation` |N|       | [Line] [Double]
        `Partial Participation` |1| - [Line] [Single]
         