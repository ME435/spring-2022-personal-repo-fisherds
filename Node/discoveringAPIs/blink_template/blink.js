// Imports
function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
}
function sleep(n) {
    msleep(n * 1000);
}
function main() {
    console.log("Ready");

    // TODO: Setup GPIO 14 as an output.

    while (true) {
        // TODO: Turn GPIO 14 on
        console.log("LED On");
        sleep(1);


        // TODO: Turn GPIO 14 off
        console.log("LED Off");
        sleep(1);

    }
}

main();
