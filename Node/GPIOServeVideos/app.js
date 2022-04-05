const express = require("express");
const Gpio = require("pigpio").Gpio;

const app = express();
app.use("/", express.static("public"));

// Pin setup
const ledRed = new Gpio(14, {
    mode: Gpio.OUTPUT
});
const ledYellow = new Gpio(15, {
    mode: Gpio.OUTPUT
});
const ledGreen = new Gpio(18, {
    mode: Gpio.OUTPUT
});
const pushbutton = new Gpio(25, {
    mode: Gpio.INPUT,
    pullUpDown: Gpio.PUD_UP,
    edge: Gpio.FALLING_EDGE
});
const servo = new Gpio(17, {
    mode: Gpio.OUTPUT
});


app.get("/hello", (req, res) => {
    res.json({
        status: "ok",
        message: "Hello World"
    });
});

app.get("/api/ledon", (req, res) => {
    console.log("Turning the LED On");
    ledRed.digitalWrite(1);
    ledYellow.digitalWrite(1);
    ledGreen.digitalWrite(1);
    res.json({
        status: "ok",
        message: "LED On"
    });
});

app.get("/api/ledoff", (req, res) => {
    console.log("Turning the LED Off");
    ledRed.digitalWrite(0);
    ledYellow.digitalWrite(0);
    ledGreen.digitalWrite(0);
    res.json({
        status: "ok",
        message: "LED Offf"
    });
});

function setLed(color, value) {

    switch (color) {
        case "r":
            ledRed.digitalWrite(value);
            break;
        case "y":
            ledYellow.digitalWrite(value);
            break;
        case "g":
            ledGreen.digitalWrite(value);
            break;
    }

}

app.get("/api/ledon/:color", (req, res) => {
    const color = req.params.color;
    setLed(color, 1);
    console.log("Turning the LED On for color " + color);
    res.json({
        status: "ok",
        message: `LED ${color} On`
    });
});

app.get("/api/ledoff/:color", (req, res) => {
    const color = req.params.color;
    console.log("Turning the LED Off for " + color);
    setLed(color, 0);
    res.json({
        status: "ok",
        message: `LED ${color} Off`
    });
});

app.get("/api/read", (req, res) => {
    res.json({
        isHigh: pushbutton.digitalRead()
    });
});

app.get("/api/servo/:pulseWidth", (req, res) => {
    const pulseWidth = req.params.pulseWidth;

    servo.servoWrite(pulseWidth);
    console.log("Turn the servo to pulseWidth " + pulseWidth);
    res.json({
        pulseWidth: pulseWidth
    });
});

app.get("/api/motor/:dutyCycle", function (req, res) {
    const dutyCycle = parseInt(req.params.dutyCycle);
    console.log("Servo for dutyCycle: " + dutyCycle);
    if (dutyCycle < 0) {
        motorA.digitalWrite(1);
        motorB.digitalWrite(0);
        motorEnable.pwmWrite(-dutyCycle);
    } else if (dutyCycle > 0) {
        motorA.digitalWrite(0);
        motorB.digitalWrite(1);
        motorEnable.pwmWrite(dutyCycle);
    } else {
        motorA.digitalWrite(0);
        motorB.digitalWrite(0);
        motorEnable.pwmWrite(0);
    }
    res.json({
        dutyCycle: dutyCycle
    });
});

app.listen(3000);