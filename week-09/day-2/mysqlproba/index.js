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

connection.query("SELECT * FROM author;", function (err,rows) {
  console.log("Data received from Db:\n");
  console.log(rows);
});
