# scripts_practica
1) doi_clean: csv contains publications.
2) refs: directory contains an examples of references txt archives.

# database
contains two tables:
1) publication: ID = int(4), title = varchar(156), doi = varchar (79);
Primary key ID

2) referebce_exp: ID = autoincrement int(4), publication = int(4), title_exp = text, doi_exp = text, title_doi = text;
primary key ID autoincrement
foreign key publication references ID publication
doi_exp and title_doi initialized NULL

# use
1) dataframe_publications: create a dataframe from the csv archive. With format (ID, title, DOI)
2) dataframe_references: create a dataframe from a directory with references in txt archives. With format (publicacionID, title exported)
3) fill_publication: adds to a database, from the publications drataframe
4) fill_reference: adds to a database, from the references drataframe, this containg a restriction

