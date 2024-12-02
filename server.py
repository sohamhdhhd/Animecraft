const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize app
const app = express();
const port = 5000;

// Enable CORS
app.use(cors());

// Middleware to parse JSON data
app.use(bodyParser.json());

// MongoDB Atlas connection string (replace with your actual MongoDB connection string)
const mongoURI = 'mongodb+srv://bak01072007:bak123456@waifu2.5ahbyyu.mongodb.net/contactFormDB?retryWrites=true&w=majority';

// Connect to MongoDB
mongoose.connect(mongoURI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.log('MongoDB connection error: ' + err));

// Define the schema for the contact form data
const contactSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  subject: String,
  message: String
});

// Create a model for the contact data
const Contact = mongoose.model('Contact', contactSchema);

// Define the POST route to handle form submission
app.post('/contact', (req, res) => {
  const { name, email, phone, subject, message } = req.body;

  const newContact = new Contact({
    name,
    email,
    phone,
    subject,
    message
  });

  // Save the data to MongoDB
  newContact.save()
    .then(() => res.status(200).send({ message: 'Data saved successfully!' }))
    .catch(err => res.status(400).send({ error: 'Error: ' + err }));
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
