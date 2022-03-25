const express = require("express")

const app = express();

app.get("/hello", (req, res) => {
    res.json({
        status: "ok",
        message: "Hello World"
    });
});

app.listen(3000);