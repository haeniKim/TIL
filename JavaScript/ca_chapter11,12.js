// chapter 11

// 함수 표현식  
// showError()

// let showError = function() {
//     console.log('error')
// }

// 함수 선언문
// showError()

// function showError() {
//     console.log('error')
// }

// 화살표 함수
// 1)
let showError = () => {
    console.log('error');
}

// 2)
const sayHello = (name) => {
    const msg = `Hello, ${name}`;
    console.log(msg);
};

sayHello("haeni");

// 3)
const add = (num1, num2) => num1+num2;

console.log(add(5, 6))



// -------------------------
// chapter 12
// 1)
const superwoman = {
    name : 'wendy',
    age : 25,
}

console.log(superwoman.name)
console.log(superwoman['age'])
console.log(superwoman)

superwoman.hairColor = 'Orange';
superwoman.Height = 165;

console.log(superwoman['Height']);

delete superwoman.Height;

console.log(superwoman);

// 2)
function makeObject(name, age) {
    return {
        name,
        age,
        hobby : 'baseball',
    }
}

const Mike = makeObject('Mike', 21);
console.log(Mike)

// 3) 객체 in 
function isAdult(user) {
    if ( !('age' in user) || user.age > 19) {
        return false;
    } 
    return true;
}

const Haeni = {
    name : 'haeni',
    age : 25,
}

const Jane = {
    name : 'jane',
}

console.log(isAdult(Haeni))
console.log(isAdult(Jane)) // 값이 없으면 함수의 조건이 undifined로 false가 되어 true가 반환되므로 조건 추가

// 4) 단축 프로퍼티
const name = 'clark';
const age = 22;

const superman = {
    name, // name = 'clark'
    age, // age = 22;
    gender: 'male',
}

// 5) for .. in 
for (k in Mike) {
    console.log(Mike[k])
}