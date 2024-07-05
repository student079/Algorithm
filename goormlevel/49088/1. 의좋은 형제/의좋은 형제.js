// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	const data = [];
	
	for await (const line of rl) {
		data.push(line);
	}
	rl.close();
	
	let [N1, N2] = data[0].split(" ").map((e) => Number(e));
	D = Number(data[1]);
	
	for (let day = 1; day <= D; day++) {
		if (day % 2 == 1) {
			let half = Math.ceil(N1/2);
			N1-=half;
			N2+=half;
		} else {
			let half = Math.ceil(N2/2);
			N2-=half;
			N1+=half;
		}
		
	
	}
	console.log(N1, N2);
	
	process.exit();
})();
