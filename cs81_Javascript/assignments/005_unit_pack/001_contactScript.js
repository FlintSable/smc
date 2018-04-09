// Problem #1 - Contacts Script
// script runs with node.js 
var contacts = require('./dataSet.json');


const contactResources = (x) => {
	let res = x.map(contact => `Company: ${contact.Company} - Phone: ${contact.Phone}`);
	return res;
	//returns array
}

console.log(contactResources(contacts));
