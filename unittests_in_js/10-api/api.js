const express = require('express');
const app = express();
const port = 7865;

app.use(express.json()); // needed to parse JSON body

// Existing routes from 9-api here...

// New GET /available_payments endpoint
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// New POST /login endpoint
app.post('/login', (req, res) => {
  const { userName } = req.body;
  if (!userName) {
    return res.status(400).send('Missing userName');
  }
  res.send(`Welcome ${userName}`);
});

// Start server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app; // export for testing
