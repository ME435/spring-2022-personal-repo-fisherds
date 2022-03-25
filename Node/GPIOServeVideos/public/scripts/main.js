var rhit = rhit || {};

rhit.ViewController = class {
	constructor() {
		console.log("Add button listeners");
		document.querySelector("#ledOnButton").onclick = (event) => {
			this.handleLedOn();
		}
		document.querySelector("#ledOffButton").onclick = (event) => {
			this.handleLedOff();
		}
	}

	handleLedOn() {
		console.log("You clicked the On button");
	}

	handleLedOff() {
		console.log("You clicked the Off button");
	}
}

rhit.main = function () {
	console.log("Ready");
	new rhit.ViewController();
};

rhit.main();
