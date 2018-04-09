function unless(test, then) {
	if (test) then();
}

function repeat(times, body) {
	for (var i = 0; i < times + 1; i++) body(i);
}

repeat(50, function(n) {

	unless(n % 3 == 2, function() {

		console.log(n, "remainder 2");

		});

});