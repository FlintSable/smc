window.onload = () => {

		var step = 50;
		var y = document.getElementById('right').offsetLeft;

		var robot = document.getElementById('robo');
		var pos;
		var posleft;
		var posright;
		console.log(pos = robot.getBoundingClientRect().left);
		console.log(pos = robot.getBoundingClientRect().right);

		document.getElementById('left').addEventListener("click", function(){
			posleft = robot.getBoundingClientRect().left;
			posright = robot.getBoundingClientRect().right;
			console.log(posleft, posright);
			pos = robot.getBoundingClientRect();
			console.log(pos);
			y = y - step;
			robot.style.left = y + "px";
		});

		document.getElementById('right').addEventListener("click", function(){
			pos = robot.getBoundingClientRect();
			console.log(pos);
			y = y + step;
			robot.style.left = y + "px";
		});

		

};



