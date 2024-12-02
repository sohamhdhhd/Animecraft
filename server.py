const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const port = 5000;

// Middleware to parse JSON data
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb+srv://bak01072007:bak123456@waifu2.5ahbyyu.mongodb.net/', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.log(err));

// Define a Schema for the contact form data
const contactSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  subject: String,
  message: String
});

const Contact = mongoose.model('Contact', contactSchema);

// POST route to save form data to MongoDB
app.post('/contact', (req, res) => {
  const { name, email, phone, subject, message } = req.body;

  const newContact = new Contact({
    name,
    email,
    phone,
    subject,
    message
  });

  newContact.save()
    .then(() => res.status(200).send('Data saved successfully'))
    .catch((err) => res.status(400).send('Error: ' + err));
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
