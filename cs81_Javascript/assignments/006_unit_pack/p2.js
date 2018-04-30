


function BankAcct(acctNum, acctOwner, checkingBalance, saveBalance, acctType){
	this.acctOwner = acctOwner;
	this.checkingBalance = checkingBalance
	this.saveBalance = saveBalance;
	this.acctType = acctType;

}

BankAcct.prototype.checkTransfer = function(amount){
	let results = amount + this.checkingBalance > 0;
	if(results){
		this.checkingBalance = this.checkingBalance - amount; 
		return 'transfer completed' + '\n' + 'New Balance:' + this.checkingBalance;
	} else {
		return 'insuficient funds';
	}
}


var SuperAccount = new BankAcct('454534', 'Elings Humloom', 100000, 100000000, 'international');
var SuperAccount2 = new BankAcct('12345', 'Roe Roger', 0, 24, 'international');


console.log(SuperAccount.checkTransfer(100));
console.log(SuperAccount2.checkTransfer(100));
