// Imports

function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
 }
 
 function sleep(n) {
    msleep(n * 1000);
 }
 
function main() {
    console.log("Ready");

    // TODO: Setup GPIO 14 (physical pin 8) as an output.

    while (true) {
        console.log("LED On");
        // TODO: Actually turn on the led
        sleep(1);

        console.log("LED Off");
        // TODO: Actually turn off the led
        sleep(1);
    }
}

main();
