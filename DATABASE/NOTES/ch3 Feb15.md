# Feb.15th Relational Model #

## Chapter 3: Relational Model Concepts ##

**Relational Model Concepts**
    *Relational Schema* `R(A.1, A.2, ..., A.n)`
        - a name:               R( )
        - a list of attributes: A.1,...A.n
        `Attribute Domain`: set of valid values for the Attribute
        [NOTE:]
            - denoted `r(R)` s.t. `r = {t.1,...t.n}` where
                - `t.i = <v.i1,...v.in>` and `v.ij ∈ Domain(A.i)`
            - degree of a relation -> number of attributes in schema

**Relational Schemas and Constraints**
    *Superkey of SK*
        a subset s.t. tuples `t.1, t.2 ∈ r(R); t.1[SK] != t.2[SK]`
            - a.k.a a Superkey UNIQUELY IDENTIFIES a TUPLE
    a `key K` of `schema R` is a `Superkey`, s.t:
        - a proper `subset of K` is `NOT a Superkey`
        - i.e. a `key K` is a `Minimal Superkey`
        *Primary Key* 
            - a key that is Chosen
        *Relational Database Schema*
            - S = {R.1,...R.n}  //has a set of integrity constraints

**Integrity Constraint**
    *Domain Constraint*
        - V.i ∈ Domain(A.i)
    *Key    Constraint*
        - Key must be Unique
    *Entity Constraint*
        - no Primary Key can be NULL
    *Referential Integrity Constraint*
        - Tuple that refers to other nested relations must refer to:
            - another existing tuple in that relation
            (i.e: STUDENT who Takes COURSE must take an existing COURSE) 

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