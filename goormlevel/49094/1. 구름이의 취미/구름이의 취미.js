// Run by Node.js
// 한변의 길이 1~N N개
// 부피 합한 값
// n**3
// N 1000000000
// 전체는 안된다
// 공식

const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	const data = [];
	for await (const line of rl) {
		if (!line) rl.close();
		data.push(line);
	}
	
	const N = BigInt(data[0]);
	const res = BigInt(((N*(N+1n))/2n)**2n) % BigInt(1000000007);
	console.log(res.toString().split("n")[0]);
	
	process.exit();
})();
