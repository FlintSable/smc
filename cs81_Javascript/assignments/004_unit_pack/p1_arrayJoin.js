
// Problem #1 

// Write a simple JavaScript program that join all elements of the following array into a string. 
// Sample array : myFaceBookFriends = ["John", "Paul", "Mary", "Tony", "Joan"];


// Expected Output: 
// "John and Paul and Mary and Tony and Joan"
// Hint: Array Method join() http://www.w3schools.com/jsref/jsref_join.asp (Links to an external site.)Links to an external site.


const arrayJoin = x => {
	if(Array.isArray(x)){
		let sentance = x.join(" and ");
		return sentance;
	} else if(!Array.isArray(x)){
		let err = "not an array";
		return err;

	}
}





let fudge = ["John", "Paul", "Mary", "Tony", "Joan"];
let doubleFudge = 21;
console.log(arrayJoin(fudge));