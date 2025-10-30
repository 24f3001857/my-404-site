// server.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('<h1>Hello from Codespaces!</h1><p>Email: 24f3001857@ds.study.iitm.ac.in</p>');
});

app.listen(8000);
// Run with: node server.js
