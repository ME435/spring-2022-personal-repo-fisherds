const Gpio = require('onoff').Gpio;


function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
}
function sleep(n) {
    msleep(n * 1000);
}
function main() {
    console.log("Ready");

    // Done: Setup GPIO 14 as an output.
    const led = new Gpio(14, 'out');

    while (true) {
        // Done: Turn GPIO 14 on
        console.log("LED On");
        led.write(1);
        sleep(1);


        // Done: Turn GPIO 14 off
        console.log("LED Off");
        led.write(0);
        sleep(1);

    }
}

main();
