CHALLENGE 1

Step 1

SELECT titles.title_id 'Title_ID', titleauthor.au_id 'Author_ID', titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 'Royalty'
FROM publications.titleauthor titleauthor
INNER JOIN publications.sales sales ON titleauthor.title_id = sales.title_id
INNER JOIN publications.titles titles ON titleauthor.title_id = titles.title_id

Step 2

SELECT titles.title_id 'Title_ID', titleauthor.au_id 'Author_ID', SUM(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) 'Royalties'
FROM publications.titleauthor titleauthor
INNER JOIN publications.sales sales ON titleauthor.title_id = sales.title_id
INNER JOIN publications.titles titles ON titleauthor.title_id = titles.title_id
GROUP BY titles.title_id, titleauthor.au_id
