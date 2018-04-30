


function BankAcct(acctNum, acctOwner, checkingBalance, saveBalance, acctType){
	this.acctOwner = acctOwner;
	this.checkingBalance = checkingBalance
	this.saveBalance = saveBalance;
	this.acctType = acctType;

}

BankAcct.prototype.checkTransfer = function(amount){
	if(amount + this.checingkBalance > 0){
		return this.checkingBalance = this.checkingBalance- amount; 
	} else {
		return 'insuficient funds';
	}
}
