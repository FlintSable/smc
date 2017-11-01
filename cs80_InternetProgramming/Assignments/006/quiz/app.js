window.addEventListener('load', function() {
	console.log("loaded");
});

function quest(){
	console.log('lets start');
	let one = prompt('hobby one: ');
	let two = prompt('hobbie two: ');
	let duck = confirm('DuckDuckGo?: ');
	let goose = '<img id="ghost" src="./duck.svg">'
	document.getElementById('one').innerHTML = one;
	document.getElementById('two').innerHTML = two;
	if(duck){
		document.getElementById('ghost').src = './duck.svg';
	}
	return;

}