var rpio = require('rpio');

function main() {
    console.log("Ready");

    // Done: Setup GPIO 14 as an output.
    let gpio14 = 8
    rpio.open(gpio14, rpio.OUTPUT, rpio.LOW);

    while (true) {
        rpio.write(gpio14, rpio.HIGH);
        console.log("LED On");
        rpio.sleep(1);
    
        rpio.write(gpio14, rpio.LOW);
        console.log("LED Off");
        rpio.sleep(1);
    }
}

main();
