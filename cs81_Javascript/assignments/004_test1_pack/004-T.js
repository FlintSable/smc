// Write a script that prompts for a string of text and alerts the 
// string made up of this value appended to itself twice. 
// For example, if the user inputs "ho", your script should alert "hohoho". 
// If the user inputs "888", your script should alert"888888888"..



let InputMult = (x) => {
	let UserInput = prompt("Enter a value");

	while( UserInput == "" ){
		UserInput = prompt("Please enter a value")
	}

	let counter = "";
	for(let i = 0; i < x; i++){
		counter += UserInput;
	}

	return counter;

};


alert(InputMult(3));
