# MARCH 1st: MIDTERM CONCISE NOTES # 

### E-R MODELING ###
    
[Attributes]
    the properties that describe an entity:
    - can be `Composite` or `Simple` (can/cannot be sub-parted)
    - can be made of one or more Values
    - can be `Stored`, or `Derived` from other attributes
    - can be made irrelevant or unknown (`NULL`)
    - can be `Complex`: (includes `Composite` and `Multi Var.`)
    - can be `Key Attributes`: (unique per entity)
    - has a  `Domain`: (all valid values that can be assigned)

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
    `Total Participation`           | [Line] [Double]
        `Partial Participation`     - [Line] [Single]

### RELATIONAL MAPPING ###

**ER-To-Relational Mapping** NOTE: Foreign Key => Foreign Key Attrib.
    *Steppies*
        **A) For Each `Entity E`:**
            1. create a `relation R.e` s.t. ∈ Simple Attributes
            2. choose one attribute as the `Primary Key`
---------------------------------------------------------------------
        **B) For Each `Weak Entity W` with `Owner Entity E`:**
            1. create a `relation R.w` s.t. ∈ Simple Attributes
            2. add `Foreign Key Attributes ∈ R.w` as `Primary Key` in
                `R.e`, that corresponds to `E`.
            3. the `Primary Key of R.w` is a combination of:
                `Primary Key R.e` and `Partial Key of W`
----------------------------------------------------------------------
        **C) For Binary `1:1` Relationship with Entities `E1 and E2`**
            1. insert the `Primary Key ∈ R.e2` as `Foreign Key ∈ R.e1`
            2. include Joint-Simple Attributes as `Attributes ∈ R.e1`
----------------------------------------------------------------------
        **D) For Binary `1:N` Relationship with Entities `E1 and E2`**
            1. insert the `Primary Key ∈ R.e1` as `Foreign Key ∈ R.e2`
            2. include Joint-Simple Attributes as `Attributes ∈ R.e2`
----------------------------------------------------------------------
        **E) For Binary `M:N` Relationship with Entities `E1 and E2`**
            1. create `relation R` ∈ All Simple Attributes/Components
            2. insert the `Primary Key ∈ R.e1`, and 
                the `Primary Key ∈ R.e2` as `Foreign Key ∈ R`
            3. `Primary Key ∈ R` is a Combination of both primary keys
----------------------------------------------------------------------
        **F) For `N-nary` Relationship with Entities `E1,...En`**
            1. create `relation R` ∈ All Simple Attributes/Components
            2. insert the `Primary Keys ∈ R.e1,...R.en` as
                 `Foreign Key ∈ R`
            3. `Primary Key ∈ R` is a Combination of ALL primary keys
----------------------------------------------------------------------
        **G) For Each `Multi-Val. Attribute A` of `Entity E`**
            1. create a `relation R.a` that includes Attribute A
            2. insert `Primary Key ∈ R.e` as `Foreign Key ∈ R.e`
            3. `Primary Key ∈ R.a` is a Combination of A and PK ∈ R.e