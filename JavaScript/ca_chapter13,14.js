// chapter 13
// method
let boy = {
    name: "Mike",
    showName: function() {
        console.log(boy.name)
    }
};

let man = boy;
man.name = "Tom"; // boy 객체의 name도 바뀜

console.log(boy.name)
man.showName();
boy.showName();

let boy2 = {
    name: "Mike",
    showName: function() {
        console.log(this.name) // this가 객체를 가리킴
    }
};

let man2 = boy2;

boy2 = null;

man2.showName();

// -------------------------
// chapter 14

// array
let days = ["mon", "tue", "wed"]

console.log(days[1]);

days.push("thu");
days.unshift("sun");

console.log(days);

for(day of days){
    console.log(day);
}

for(let index=0;index<days.length;index++) {
    console.log(days[index]);
}