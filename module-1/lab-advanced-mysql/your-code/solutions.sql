CHALLENGE 1

Step 1

SELECT titles.title_id AS Title_ID, titleauthor.au_id AS Author_ID, (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS Royalty
FROM publications.titleauthor titleauthor
INNER JOIN publications.sales sales ON titleauthor.title_id = sales.title_id
INNER JOIN publications.titles titles ON titleauthor.title_id = titles.title_id

Step 2

SELECT titles.title_id AS Title_ID, titleauthor.au_id AS Author_ID, SUM(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS Royalties
FROM publications.titleauthor titleauthor
INNER JOIN publications.sales sales ON titleauthor.title_id = sales.title_id
INNER JOIN publications.titles titles ON titleauthor.title_id = titles.title_id
GROUP BY Title_ID, Author_ID

Step 3
#En este paso, me muestra 3 autores, pero no me los ordena por Profits, y no sé por qué. He probado diferentes cosas pero no he conseguido nada.

SELECT titleauthor.au_id AS Author_ID, SUM(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS Profits
FROM publications.titleauthor titleauthor
INNER JOIN publications.sales sales ON titleauthor.title_id = sales.title_id
INNER JOIN publications.titles titles ON titleauthor.title_id = titles.title_id
GROUP BY Author_ID
ORDER BY Profits DESC
LIMIT 3

CHALLENGE 2

Step 1
