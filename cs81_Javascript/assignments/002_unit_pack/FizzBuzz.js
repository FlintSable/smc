// Nicholas Noochla-or 3/18/1990

// javascript arrow function
let switcheroo = x => {
	// tricky switch statement for practice
	switch(true){
		case x%4 === 0 && x%10 === 0:
			return "FizzBuzz"
			break;
		case x%4 === 0:
			return "Fizz";
			break;
		case x%10 === 0:
			return "Buzz";
			break;
		default:
			return x;
	}
}

let fizzbuzz = f => {
	for(let i = 0; i < f; i++){
		console.log(switcheroo(i));
	}
}

fizzbuzz(121);