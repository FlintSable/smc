// Problem #3


function Person(firstName, mother, father, spouse, children){
	this.firstName = firstName;
	this.mother = mother;
	this.father = father;
	this.spouse = spouse;
	this.children = children;
	this.changeSpouse = function(name){
		this.spouse = name;
		return this.spouse;
	}
};

let ani = new Person("Ani", "NA", "NA", "Sipho", ["Aolani", "Hiro", "Xue"]);
let tuulia = new Person("Tuulia", "NA", "NA", ["Sipho"]);
let sipho = new Person("Sipho", "Tuulia", "NA", "Ani", ["Aolani", "Hiro", "Xue"])


console.log(sipho.mother); 
ani.changeSpouse("mars");
console.log(ani.spouse);


