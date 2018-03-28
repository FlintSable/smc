
$(window).on("load", function() {

	var breakfast = prompt("What would you like for breakfast?");

	var addFast = () => {

			var newDiv = document.createElement("div");
			newDiv.setAttribute("style", "color:#FFDC00; font-size:12em; font-family:helvetica;");
	    	var node = document.createTextNode(`${breakfast}`);
			newDiv.appendChild(node);
			var inPlaceDiv = document.getElementById("div1");
			document.body.insertBefore(newDiv, inPlaceDiv);
	}

	addFast();

});
