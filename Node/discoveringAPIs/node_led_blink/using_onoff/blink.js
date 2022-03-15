const Gpio = require('onoff').Gpio;

function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
 }
 
 function sleep(n) {
    msleep(n * 1000);
 }

function main() {
    console.log("Ready");

    const led = new Gpio(14, 'out');

    while (true) {
        console.log("LED On");
        led.write(1);
        sleep(1);

        console.log("LED Off");
        led.write(0);
        sleep(1);
    }
}


main();
