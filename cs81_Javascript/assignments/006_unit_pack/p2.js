


function BankAcct(acctNum, acctOwner, checkingBalance, saveBalance, acctType){
	this.acctOwner = acctOwner;
	this.checkingBalance = checkingBalance
	this.saveBalance = saveBalance;
	this.acctType = acctType;

}

BankAcct.prototype.checkTransfer = function(amount){
	let accountChk = (amount + this.checingkBalance) > 0
	if(accountChk){
		this.checkingBalance = this.checkingBalance - amount; 
		console.log(this.checkingBalance);
	}
}


var EagleAccount = new BankAcct('435465', 'Elias Herloom', 1000000, 100000000, 'Silver');

console.log(EagleAccount.checkTransfer());