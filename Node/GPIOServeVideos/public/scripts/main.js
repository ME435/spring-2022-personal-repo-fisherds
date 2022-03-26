var rhit = rhit || {};

rhit.ViewController = class {
	constructor() {
		console.log("Add button listeners");
		document.querySelector("#redLedOnButton").onclick = (event) => {
			this.handleLedOn("r");
		}
		document.querySelector("#redLedOffButton").onclick = (event) => {
			this.handleLedOff("r");
		}
		document.querySelector("#yellowLedOnButton").onclick = (event) => {
			this.handleLedOn("y");
		}
		document.querySelector("#yellowLedOffButton").onclick = (event) => {
			this.handleLedOff("y");
		}
		document.querySelector("#greenLedOnButton").onclick = (event) => {
			this.handleLedOn("g");
		}
		document.querySelector("#greenLedOffButton").onclick = (event) => {
			this.handleLedOff("g");
		}
		document.querySelector("#readButton").onclick = (event) => {
			this.handleRead();
		}
	}

	async handleLedOn(color) {
		console.log("You clicked the On button for " + color);
		const response = await fetch("/api/ledon/" + color);
		const data = await response.json();
		console.log("Response", data);
	}

	async handleLedOff(color) {
		console.log("You clicked the Off button for " + color);
		const response = await fetch("/api/ledoff/" + color);
		const data = await response.json();
		console.log("Response", data);
	}

	async handleRead() {
		const response = await fetch("/api/read");
		const data = await response.json();
		console.log("Response", data);
		document.querySelector("#buttonStatus").innerHTML = `The pushbutton is ${data["isHigh"] ? "HIGH" : "LOW"}`;
	}
}

rhit.main = function () {
	console.log("Ready");
	new rhit.ViewController();
};

rhit.main();
