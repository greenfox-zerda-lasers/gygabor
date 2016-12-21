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

connection.query("SELECT book_name FROM book_mast;", function (err,rows) {
  console.log("Data received from Db:\n");
  console.log(rows);
});

connection.query("SELECT book_name, aut_name FROM book_mast JOIN author ON book_mast.aut_id = author.aut_id;", function (err,rows) {
  console.log("Data received from Db:\n");
  console.log(rows);
});
