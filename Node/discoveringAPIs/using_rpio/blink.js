// https://github.com/jperkin/node-rpio
rpio = require("rpio");

function main() {
    console.log("Using RPIO");
    const gpio14 = 8;

    rpio.open(gpio14, rpio.OUTPUT, rpio.LOW)

    while(true) {
        console.log("LED on");
        rpio.write(gpio14, rpio.HIGH);
        rpio.sleep(1);
        console.log("LED off");
        rpio.write(gpio14, rpio.LOW);
        rpio.sleep(1);
    }
}


main()