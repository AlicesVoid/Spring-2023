# April 10.th Database Notes #    
  
## CH.9 FILE STRUCTURES ##    
  
### Secondary Storage  
 **Parts:**  
    - Track 
    - Sector 
    - Cylinder   
 **Calculations:**  
    - *Assume we have # records, each has 2^# bytes*  
    `Total Number of Tracks:`
        - records per sector -> # of sectors -> # of tracks
    `Track Reading Time`
        - Seek Time + Rotational Delay + Transfer Time 
    `Seek Time:`   
        - read/write head on track   
    `Rotational Delay (latency):`   
        - first sector (block) under head   
    `Block Transfer Time:`   
        - read/write one block (blocks are disck files)   
 **Worst Scenario Calculations:** 
    - *Assume we are using Random Storage*
    `Number of Sectors in a Cluster:`
        - minimum reading time -> cluster -> # of sectors
  
### Streaming Files in Code  
 **Using C:**  
    - use a C struct (to get a row using char[]s)
 **Using C++:**  
     - use a C++ class (to get a row using char[]s)  
   
### I/O Overloading    
 **istream & operator >> :**  
    - `(istream &is, Person &p) {is.getline(p.item); return is;};`  
 **ostream & operator << :**
    - `(ostream &os, Person &p) {os << p.item << endl; return os;};`
  
### Field Structures  
 **Types:**  
    - `Fixed Length:` each field has an exact length  
    - `Length Indicators:` each field starts with a len. indicator (num)  
    - `Delimiters:` each field is separated by a delimiter `|`  
    - `Keywords:` each field is written as `keyword=value`  
    - `Index File:` uses the literal index number for each field location  
 **Advantages/Disadvantages:**  
    - consider if you need to save time or space   
    - consider the weight of efficiency   
    - consider information already included in the data-set  