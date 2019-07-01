var $ = function(id) {
    return document.getElementById(id);
};

var $ = function(id) {
    return document.getElementById(id);
};

var processEntry = function() {
	var entry = $("cents").value;         // get user entry
    var cents = parseInt(entry);          // parse entry
	makeChange(cents);
	$("cents").focus();
};

var makeChange = function(cents) {
	var quarters = parseInt(cents / 25);  // get number of quarters

	var dimes = 0;                        // get number of dimes

	var nickels = 0;                      // get number of nickels
	
	var pennies = 0;                      // get number of pennies
	
	// display the results of the calculations
	$("quarters").value = quarters;
	$("dimes").value = dimes;
	$("nickels").value = nickels;
	$("pennies").value = pennies;
};

window.onload = function () {
    $("calculate").onclick = processEntry;
	$("cents").focus();
};
