var spawn = require("child process").spawn,child;
child = spawn("powershell.exe",["C:\\whereisfile.ps1"]);
child.stdout.on("data", function(data){
	console.log("Ppowershell Data: " + data);
});

child.stderr.on("data", function(data){
	console.log("Powershell Errors: " + data);
});

child.on("exit", function(){
	console.log("Powershell Script finished");
});
child.stdin.end();



// powershell node
// http://rannn505.github.io/node-powershell/