
// Example constructor function
function Passenger(first, last, age, seatNumber, bags, medicalHistory){
	this.firstName = first;
	this.lastName = last; 
	this.age = age;
	this.seatNumber = seatNumber; 
	this.bags = bags;
	this.medicalHistory = medicalHistory;
}; 


function checkGivenProperty(obj, prop){
	return ({}).hasOwnProperty.call(obj, prop);
	
};

function checkGivenPropertyUndefined(obj, prop){
	if(checkGivenProperty(obj,prop)){
		if(obj.prop === undefined){
			return true;
		} else {
			return false;
		};	
		
	};
	
};

// example user object
var RoeRoger = new Passenger('row', 'rogger', 55, 'B12', 4);

// calling the Object Propety checker
// in this case all the object created with this constructor 
// will have the property modicalHistory

checkGivinProperty(RoeRoger, 'medicalHistory');
checkGivenPropertyUndefined(RoeRoger, 'medicalHistory');



