
let shuttle = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

const revArray = (x) => {
	let rev = [];
	let count = 0;
	for(let i = 0; i < x.length; i++){
		count += 1;
		rev.push(x[x.length - count]);
	}
	return rev;

} 

console.log(revArray(shuttle));