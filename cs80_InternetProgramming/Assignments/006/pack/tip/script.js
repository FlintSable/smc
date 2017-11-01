window.addEventListener('load', function() {
	console.log("loaded");



});



function KeyUpBill(){
	CalcTotal();
}

function KeyUpTip(){
	CalcTotal();

}

function KeyUpPeep(){
	CalcTotal();
}

function CalcTotal(){
	let bill = document.getElementsByClassName("BillBox");
	bill = bill[0].value;
	let tip = document.getElementsByClassName("TipPer");
	tip = tip[0].value;
	let numpeep = document.getElementsByClassName("NumPeep");
	numpeep = numpeep[0].value;

	console.log('Bill: ' + bill);
	console.log('Tip %: ' + tip);
	console.log('Number of People: ' + numpeep);
	console.log('TIP: ' + parseInt(bill) * (parseInt(tip)/100));
	console.log('TOTAL: ' + parseInt(bill) * ((parseInt(tip)/100) / parseInt(numpeep)));

	


}