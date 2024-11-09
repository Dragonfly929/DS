const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

const palettes = {};  // In-memory data storage for palettes' popularity

app.get("/status", (req, res) => {
    res.json({ status: "running" });
});

app.get("/palettes/:paletteId", (req, res) => {
    const paletteId = req.params.paletteId;
    const palette = palettes[paletteId];
    if (palette) {
        res.json(palette);
    } else {
        res.status(404).json({ error: "Palette not found" });
    }
});

app.post("/like", (req, res) => {
    const { paletteId } = req.body;
    if (!palettes[paletteId]) {
        palettes[paletteId] = { likes: 0 };
    }
    palettes[paletteId].likes += 1;
    res.json({ paletteId, likes: palettes[paletteId].likes });
});

function registerService() {
    const registerUrl = process.env.REGISTER_URL;
    axios.post(registerUrl, {
        service_name: "popularity-service",
        instance_url: "http://popularity-service:6000"
    })
    .then(() => console.log("Registered popularity-service"))
    .catch(err => console.error("Error registering service:", err));
}

registerService();

app.listen(6000, () => {
    console.log("Popularity service running on port 6000");
});
