// chapter 9 - switch

// apple : 100won
// banana : 200won
// kiwi : 300won
// melon : 500won
// watermelon :500 won

let fruit = prompt('which fruit do you want to buy?');

switch(fruit){
    case 'apple':
        console.log('100won');
        break
    case 'banana':
        console.log('200won');
        break
    case 'kiwi':
        console.log('300won');
        break
    case 'melon':
    case 'watermelon':
        console.log('500won');
        break;
    default :
        console.log('there are no such fruit')
}

// -------------------------
// chapter 10

// no argument
function showError(){
    alert('에러 발생. 다시 시도해주세요.')
}

showError();

// 1 argument
let msg = 'Hello'; // 전역 변수
console.log(msg)

function sayHello(name) {
    if (name) { // name 인수에 값을 주지 않으면 undefined -> false
        msg += `, ${name}`;
    }
    console.log(msg);
}

sayHello('Haeni');
sayHello();
console.log(msg)

// 전역 변수, 지역 변수
let msg2 = "welcome";
console.log(msg2); // "welcome"

function sayBye(name){
    let msg2 = "Bye";
    console.log(msg2 + ' ' + name); //"Bye name"
}

sayBye("haeni");
console.log(msg) //"welcome"

// or 연산자 활용 <-- 다시 보기
function sayHello2(name) {
    let newName = name || 'friend'; // 매개변수를 입력하지 않으면 true값인 'friend' 반환
    let msg3 = `Hello, ${newName}`
    console.log(msg3);
}

// default 활용
function sayHello2(name = 'friend') { 
    let msg3 = `Hello, ${name}`
    console.log(msg3);
}

sayHello2('Haeni');
sayHello2();

// return 값 반환
function add(num1, num2) {
    return num1 + num2;
}

const result = add(3,4);
console.log(result)

