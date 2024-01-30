// chapter 7

//or, 이름이 TOM 이거나 성인이면 통과
const name = "Mike";
const age = 30;

if(name === "TOM" || age > 19){
    console.log('통과');
}

//or, 이름이 Mike이고  성인이면 통과
const name2 = "Mike";
const age2 = 30;

if(name2 === "Mike" && age2 > 19){
    console.log('통과');
}

// not, 나이를 입력받아 성인 아니면 돌아가
//const age3 = prompt('나이 ? : ')
//const isAge = age > 19;

//if (!isAge){
//    console.log('돌아가')
//}

// 우선순위 and > or
// 남자이고, 이름이 Mike 거나 성인이면 통과

const gender = 'F';
const name3 = 'Jane';
const isAdult = true;

if(gender === 'M' && (name === 'Mike' || isAdult)) {
    console.log('통과');
} else {
    console.log('go back');
}

// -------------------------
// chapter 8

// for문

// 1부터 10까지 로그
for (let i = 1; i <= 10; i++) {
    console.log(i)
}

// while문
let i = 1;

while(i<11) {
    console.log(i);
    i++;
}

// break
while(true) {
    let answer = confirm('continue?')
    if (!answer) {
        break
    }
}

// continue
for(let i = 0;i<10;i++) {
    if (i % 2) { // i % 2 -> 0이면 false로 계산
        continue;
    } else {
        console.log(i);
    }
}