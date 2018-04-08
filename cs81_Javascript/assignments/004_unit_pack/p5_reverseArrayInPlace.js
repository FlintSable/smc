// reverse an array in place

let shuttle = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

const revArray = (x) => {
	let front;
	for(let i = 0; i < x.length; i++){
		// console.log(x[x.length - 1]);
		front = x[x.length - 1];
		x.unshift(front);
		x.pop();
		console.log(x);
	}
	return x;

} 

console.log(revArray(shuttle));