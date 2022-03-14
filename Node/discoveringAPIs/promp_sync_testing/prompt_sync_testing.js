var prompt = require('prompt-sync')();


function main() {
    console.log("Ready");

    while (true) {
        var name = prompt('What is your name? ');
        console.log(`Hello, ${name}`);
        if (!name) {
            console.log("Goodbye");
            break;
        }
    }
}

main()