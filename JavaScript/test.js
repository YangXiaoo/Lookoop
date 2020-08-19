let s = "hello"
s = s + " world"

let objArr = [
	{
		name: 's'
	},
	{
		name: 'a'
	}
]

for (let i of objArr) {
	console.log(i)
	for (let obj in i) {
		console.log(i)
	}
}