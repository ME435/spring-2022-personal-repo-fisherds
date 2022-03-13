// Imports
function msleep(n) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, n);
 }
 
 function sleep(n) {
    msleep(n * 1000);
 }

function main() {
    console.log("Ready");
    while(true) {
        console.log("LED on");
        sleep(1);
        console.log("LED off");
        sleep(1);
    }
}


main()