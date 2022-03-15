// Imports

function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
 }
 
 function sleep(n) {
    msleep(n * 1000);
 }

function main() {
    console.log("Ready");

    // TODO: Set GPIO 14 as an output

    while (true) {
        console.log("LED On");
        // TODO: Turn the LED on using a library
        sleep(1);

        console.log("LED Off");
        // TODO: Turn the LED off using a library
        sleep(1);
    }
}


main();
