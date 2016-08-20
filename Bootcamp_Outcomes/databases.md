
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
1. **One-to-one:** Both tables can have only one record on either side of the relationship. Each primary key value relates to only one (or no) record in the related table. 