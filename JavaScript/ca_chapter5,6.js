// chapter 5
let  num = 10;

num += 4;
num++;
num++;
num--;

console.log(num);

let result = num++; // 1을 증가시키기 전의 값이 result에 할당

console.log(result);

// -------------------------
// chapter 6

console.log(10 > 5);
console.log(10 == 5);
console.log(10 != 5);

// 동등 연산자
console.log(1 == "1");

// 일치 연산자
console.log(1 === "1");

// 조건문
const age = 19;

if(age > 19) {
    console.log('환영합니다');
}

if(age <= 19){
    console.log('안녕히 가세요');
}

console.log('-------------------------')

if(age > 19) {
    console.log('환영합니다');
} else if (age === 19) {
    console.log('수능 잘 치세요');
} else {
    console.log('안녕히 가세요');
}