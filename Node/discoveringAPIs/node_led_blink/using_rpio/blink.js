// Imports
var rpio = require('rpio');

function main() {
    console.log("Ready");
    let gpio14 = 8;
    rpio.open(gpio14, rpio.OUTPUT, rpio.LOW);
    while (true) {
        console.log("LED On");
        rpio.write(gpio14, rpio.HIGH);
        rpio.sleep(1);

        console.log("LED Off");
        rpio.write(gpio14, rpio.LOW);
        rpio.sleep(1);
    }
}


main();
