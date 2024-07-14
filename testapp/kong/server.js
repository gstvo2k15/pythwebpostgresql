const express = require('express');
const app = express();
const PORT = 1337;

app.get('/', (req, res) => {
  res.send('Hello from Konga!');
});

app.listen(PORT, () => {
  console.log(`Konga is running on port ${PORT}`);
});

