SELECT authors.au_id 'AUTHOR ID', authors.au_lname 'LAST NAME', authors.au_fname 'FIRST NAME', titles.title_id 'TITLE', publishers.pub_id 'PUBLISHER'
FROM publications.authors authors
LEFT JOIN publications.titleauthor titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN publications.titles titles
ON titleauthor.title_id = titles.title_id
LEFT JOIN publications.publishers publishers
ON titles.pub_id = publishers.pub_id
