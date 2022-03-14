const Gpio = require('pigpio').Gpio;


function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
}
function sleep(n) {
    msleep(n * 1000);
}
function main() {
    console.log("Ready");

    // TODO: Setup GPIO 14 as an output.
    const led = new Gpio(14, {mode: Gpio.OUTPUT});

    while (true) {
        // TODO: Turn GPIO 14 on
        console.log("LED On");
        led.digitalWrite(1);
        sleep(1);


        // TODO: Turn GPIO 14 off
        console.log("LED Off");
        led.digitalWrite(0);
        sleep(1);

    }
}

main();
