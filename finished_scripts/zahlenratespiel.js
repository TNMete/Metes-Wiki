const prompt = require("prompt-sync")();
const secretNumber = Math.floor(Math.random() * 100) + 1;

console.log("I've chosen a number, gl with your choice!");

function guessNumber() {
    let richtig = false;

    while (!richtig) {
        let chosenNumber = prompt("Guess my number:");
        chosenNumber = Number(chosenNumber);

        if (chosenNumber < secretNumber) {
            console.log("Think bigger!");
            // alert("Think bigger!");
        } else if (chosenNumber > secretNumber) {
            console.log("You're thinking too big, my friend!");
            // alert("You're thinking too big, my friend!");
        } else {
            console.log("Jackpot!");
            // alert("Jackpot!");
            richtig = true;
        }
    }
}
guessNumber();
