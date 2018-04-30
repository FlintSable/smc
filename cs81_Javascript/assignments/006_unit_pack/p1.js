


function Employee(first, last, ssn, eid, dept){
	this.firstName = first;
	this.lastName = last;
	this.ssn = ssn;
	this.eid = eid;
	this.dept = dept;		
		
}

Employee.prototype.ssn = "000-00-0000";
Employee.prototype.dept = "empty";
Employee.prototype.fullName = function(){
	return this.firstName + ' ' + this.lastName;
};


var eRichRoe = new Employee("Richard","Roe","123-34-1234","001234", "acct");

var eSallyRally = new Empoyee("Sally", "Rally", "123-34-1235", "001235","hr")
