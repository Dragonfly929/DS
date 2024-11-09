const express = require('express');
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/popularity_db', { useNewUrlParser: true });

const app = express();
app.use(express.json());

app.post('/like', (req, res) => {
    const { user_id, palette_id } = req.body;
    // Logic to add like
    res.status(200).json({ message: 'Palette liked successfully' });
});

app.get('/popular', (req, res) => {
    // Fetch most popular palettes
    res.json([{ palette_id: 1, likes: 100 }]);
});

app.listen(3001, () => console.log('Popularity Service running on port 3001'));
