// Nicholas Noochla-or March 25, 2018 
// cs 81 1729 JavaScript


// pass the function three or more values and it will return the maximum
var maxx = (a, b, ...others) => {
	let MaxValue; 
	if(a < b){
		MaxValue = b;
	}else if(a > b){
		MaxValue = a;
	}

	for(let val of others){
		if(MaxValue < val){
			MaxValue = val;
		}
	}

	return MaxValue;

};


console.log(maxx(2, 1, 1, 60, 100000000, 55, 100, 200, 1, 3, 4, 9, 5, 345));