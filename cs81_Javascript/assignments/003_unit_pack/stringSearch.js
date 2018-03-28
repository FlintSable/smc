// Nicholas Noochla-or March 25, 2018 
// cs 81 1729 JavaScript


// pass the function two arguments. The first a string and the seccond a letter to look for
// it will return the occurrence of that letter from the first argument
var stringSearch = (a, b) => {
	let occurrence = 0; 
	a = a.toLowerCase();
	for(let i = 0; i < a.length; i++){
		if(a[i] === b){
			occurrence++;
		}
	}

	return occurrence;

};


console.log(stringSearch('ZenZizenziZenzic','z'));