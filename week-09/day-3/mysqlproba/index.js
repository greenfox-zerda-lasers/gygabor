var mysql = require("mysql");

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'cookies',
  database: 'bookstore'
});

connection.connect(function (error){
  if (error) {
    console.log('muhahaha', error);
  } else {
    console.log ('WOOOOWW');
  }
});

// connection.query("SELECT book_name FROM book_mast;", function (err,rows) {
//   console.log("Data received from Db:\n");
//   console.log(rows);
// });
//
// connection.query("SELECT book_name, aut_name FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id;", function (err,rows) {
//   console.log("Data received from Db:\n");
//   console.log(rows);
// });

// connection.query("SELECT book_name, aut_name, cate_descrip FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id;", function (err,rows) {
//   console.log("Data received from Db:\n");
//   console.log(rows);
// });

// connection.query("SELECT book_name, aut_name, cate_descrip, pub_name FROM book_mast INNER JOIN author ON book_mast.aut_id = author.aut_id INNER JOIN category ON book_mast.cate_id = category.cate_id INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id;", function (err,rows) {
//   console.log("Data received from Db:\n");
//   console.log(rows);
// });

connection.query("SELECT book_name, aut_name, cate_descrip, book_price pub_name FROM book_mast INNER JOIN author ON book_mast.aut_id = author.aut_id INNER JOIN category ON book_mast.cate_id = category.cate_id INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id;", function (err,rows) {
  console.log("Data received from Db:\n");
  console.log(rows);
});
