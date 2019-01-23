CHALLENGE 1

Step 1

SELECT titles.title_id 'Title ID', authors.au_id 'Author ID', titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 'sales_royalty'
FROM publications.authors authors
INNER JOIN publications.titleauthor titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN publications.titles titles ON titleauthor.title_id = titles.title_id
INNER JOIN publications.sales sales ON titles.title_id = sales.title_id

Step 2


