// Problem #2 

// Write a range function that takes two arguments, start and end, and returns an array containing all the numbers from start up to (and including) end.

// Next, write a sum function that takes an array of numbers and returns the sum of these numbers. Run the previous program and see whether it does indeed return 55.

// console.log(range(1, 10));
// //  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// console.log(sum(range(1, 10)));
// // 55


const range = (x, y, z) => {
	let ranger = [];


	if(x < y){
		for(let i = x; i < y + z; i += z){
			ranger.push(i);
		}
		if(Array.isArray(ranger)){
			return ranger;
		}
	} else if(x > y){
		for(let i = x; i > y - 1; i--){
			ranger.push(i);
		}
		return ranger;
	} else if(x == y){
		return "err";
	} else {
		let err = "incorrect arguments";
		return err;
	}
	
};

const summ = (x) => {
	let total = 0;
	if(Array.isArray(x)){
		for(let i of x){
			total += i;
		}
	}
	return total;

}



console.log(summ(range(1, 10, 2)));


