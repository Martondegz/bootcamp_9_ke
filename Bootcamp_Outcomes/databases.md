
## Databases  

#### What's a database?  

A database is a collection of indexed or organized data usually as a group of linked files that allows easy retrieval, updating, analysis and output of data. The data stored could be in the form of graphics, reports, scripts, tables, representing almost every kind of information. Most applications in fact are databases at their core, e.g. Word processors, spreadsheets etc.  
To access information from a database, you need a database management system (DBMS). This is a collection of programs that enables you to enter, organize and select data in a database. The DBMS acts as the interface between end users and the database itself, thus masking sure data is constantly organized and accessible by other applications and users.  
Databases are classified according to their type of content, application and technical aspect. E.g. a graph database uses graph structures to represent and store information.  

A DBMS always provides data independence. Any change in mechanism and formats are performed without modifying the entire application. There are four main types of db organizations:  

1. Relational Database: Data is organized as logically independent tables. Relationships among tables are shown through shared data. The data in one table may reference similar data in other tables, which maintains the integrity of the links among them. This is also the most widely used system of db organization.  
2. Flat Database: Data is organized in a single kind of record with a fixed number of fields. This db type encounters more errors due to the repetitive nature of data.  
3. Object Oriented Database: Data is organized with similarity to object oriented programming concepts. An object consisting of data and methods, while classes group objects having similar data and methods.  
4. Hierarchical Database: Data is organized with hierarchical relationships. It becomes a really complex network if the one to many relationship is violated.  

#### Differences between SQL and NOSQL databases  

###### SQL(Structured Query Language)  
SQL is a standard interactive and programming language for getting information from and updating a database. Although it's both an ANSI and ISO standard, many db products support SQL.  

###### So What's an SQL Database?  

Talking about an SQL db, the basic concept is that it's a Relational database. Relational dbs strictly use realtions(frequently called tables) to store data. The resulting group of tables is known as a **Schema**.  
Examples of SQL databases:  
1. MySQL  
2. Oracle Express Edition  
3. Postgres

###### Limitations for SQL Databases:  
1. Scalability:  
> Users have to scale relational database on powerful servers that are expensive and difficult to handle. To scale a relational db, it has to be distributed on multiple servers thus handling might be total chaos!  

###### NOSQL Databases  

NoSQL encompasses a wide variety of different database technologies that were developed in response to the demands presented in building modern applications. NoSQL dbs are sometimes referred to as cloud databases, non-relational databases, Big Data databases in response to sheer volume of data being generated, stored and analyzed by modern users.
The basic quality of NoSQL is that, it may not require fixed table schemas and have a lot of restrictions.  
Examples of NoSQL databases:  
1. MongoDB  
2. CouchDB  
3. Redis


###### Advantages of NoSQL databases:  
1. NoSQL dbs generally process data faster than relational databases.  
2. NoSQL dbs present simple data models.  
3. Major NoSQL systems are flexible enough to better enable devs to use applications in ways that meet their needs.  



#### Relationships.  

A relationship is a situation that exists between two relational database tables when one table has a foreign key that references the primary key of the other table. They allow relational dbs to split and store data in different tables, while linking disparate data items.  

##### Relationship types:  
1. **One-to-one:** Both tables can have only one record on either side of the relationship. Each primary key value relates to only one (or no) record in the related table. they're like spouses -you may or may not be married, but if you are, both of you and your spouse have only one spouse.  

2. **One-to-many:** The primary key table contains only one record that relates to none, one, or many records in the related table. This relationship is similar to the one between you and a parent. You only have one mother, but your mother may have several children.  

3. **Many-to-many:** Each record in both tables can relate to any number of records (or no records) in the other table. For instance, if you have several siblings, so do your siblings(have many siblings). Many-to-many relationships require a thid table known as an associate or linking table, because relational systems can't directly accomodate the relationship.  

Those matching values are the primary and foreign key values.(The relational model doesn't require that a relationship be based on a primary key.) You can use any candidate key in the table, but using the primary key is the accepted standard. A **primary key** uniquely identifies each record in a table. A **foreign key** simply puts one table's primary key in another table. Thus one just simply adds the primary jey field to the related table, as a foreign key.  

The only consideration is that a foreign key must be of the same data type as the primary key. In addition, foreign keys can be Null.  

##### Database Queries  

A query is a request for information from a database. Many database systems allow one to make requests for information in the form of a stylized query, that must be writtern in a special query language.  
An appendix of commonly used commands:
1. **ALTER TABLE**  
```ALTER TABLE table_name ADD column datatype```  
ALTER TABLE lets you add columns to a table in a database.  

2. AND
``` SELECT column_name FROM table_name
	WHERE column_1 = value_1
	AND column_2 = value_2;
```
AND is an operator that combines two conditions. Both conditions must be true for the row to be included in the result set.  

3. COUNT
``` SELECT COUNT(column_name) FROM TABLE table_name```
COUNT() is a function that takes the name if a column as an argument and counts the number of rows where the column is NULL.  

4. CREATE TABLE  
``` CREATE TABLE table_name(column_1, column_2 datatype, column_3 datatype); ```
CREATE TABLE creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.  

5. DELETE
``` DELETE FROM table_name WHERE some_column = some_value; ```
DELETE statements are used to remove rows from a table.  

#### SQL Data types:  

 | Data Type 		| Description 						|
 | ---------------- |:---------------------------------:|
 | CHARACTER		| Character string. Fixed length n  |
 | BINARY			| Binary string. Fixed length n  |
 | VARCHAR(n)		| Character string. Variable length. max length n  |
 | BOOLEAN			| Stores True or False values  |
 | INTEGER(p)		| Integer numerical (no decimal). Precision p  |
 | SMALLINT			| Integer numerical (no decimal). precision 10  |
 | BIGINT			| Integer numerical (no decimal). precision 19  |
 | FLOAT			| Approximate numerical mantissa precision 16  |
 | DOUBLE PRECISION	| Approximate numerical mantissa precision 16  |
 | DATE				| Stores year, month and day values  |
 | TIME				| Stores year, month and day values  |
 | TIMESTAMP		| Stores year, month, day, hour, minute and second values  |
 | ARRAY			| A set-length and ordered collection of elements  |
 