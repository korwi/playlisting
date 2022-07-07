function reversed(x){
    return x.reverse();
};

function isInt(n){
    return Number(n) === n && n % 1 === 0;
};

function testIsInt(){
    let outp = [isInt(6),
                isInt(6.3),
                isInt(25436),
                isInt(2356.23464),
                isInt(0),
                isInt(-0.2135),
                isInt(-1253)];
    let answ = [true, false, true, false, true, false, true];
    if (outp === answ){
        console.log("✅ testIsInt passed the test");
    } else {
        console.log("⛔️ testIsInt failed the test");
    };
};

function isFloat(n){
    return Number(n) === n && n % 1 !== 0;
};

function testIsFloat(){
    let outp = [isInt(6), 
                isInt(6.3),
                isInt(25436),
                isInt(2356.23464),
                isInt(0),
                isInt(-0.2135),
                isInt(-1253)];
    let answ = [false, true, false, true, false, true, false];
    if (outp === answ){
        console.log("✅ testIsInt passed the test");
    } else {
        console.log("⛔️ testIsInt failed the test");
    };
};

function timeParser(x) {
    if (x instanceof Array) {
        let days_grammar = (parseInt(x[3])===1) ? "Day" : "Days";
        let hours_grammar = (parseInt(x[2])===1) ? "Hour" : "Hours";
        let minutes_grammar = (parseInt(x[1])===1) ? "Minute" : "Minutes";
        let seconds_grammar = (parseInt(x[0])===1) ? "Second" : "Seconds";

        let days_final = (parseInt(x[3])>0) ? `${parseInt(x[3])} ${days_grammar}, ` : ``;
        let hours_final = (parseInt(x[2])>0) ? `${parseInt(x[2])} ${hours_grammar}, ` : ``;
        let minutes_final = (parseInt(x[1])>0) ? `${parseInt(x[1])} ${minutes_grammar}, ` : ``;
        let seconds_final = (parseInt(x[0])>0) ? `${parseInt(x[0])} ${seconds_grammar}` : ``;
        return days_final+hours_final+minutes_final+seconds_final;
    } else if((isInt(x)) || (isFloat(x))) {
        // good luck understanding
        return  time_parser([x%60, (((Math.floor(x/60))%60, (Math.floor(Math.floor(x/60))/60)%60), Math.floor((Math.floor(Math.floor(x/60))/60)/24))%24]);
    };
};

function testTimeParser(){
    let outp = [timeParser([37, 2, 0, 0]),
                timeParser([0, 2, 23, 0]),
                timeParser([435, 2, 0, 0]),
                timeParser([37, 4356, 0, 0]),
                timeParser([37, 2, 34, 34]),
                timeParser([37, 2, 23, 3]),
                timeParser([59, 59, 23, 2]),
                timeParser([333, 2345, 2345, 2345])];
    let answ = ["2 Minutes, 37 Seconds",
        "23 Hours, 2 Minutes, ",
        "2 Minutes, 435 Seconds",
        "4356 Minutes, 37 Seconds",
        "34 Days, 34 Hours, 2 Minutes, 37 Seconds",
        "3 Days, 23 Hours, 2 Minutes, 37 Seconds",
        "2 Days, 23 Hours, 59 Minutes, 59 Seconds",
        "2345 Days, 2345 Hours, 2345 Minutes, 333 Seconds"];
    if (outp === answ){
        console.log("✅ testIsInt passed the test");
    } else {
        console.log("⛔️ testIsInt failed the test");
    };
};

function sumUnLists(...args) {
    let c = [0, 0, 0, 0];
    for (var list in args){
        for (var [n, i] of list) {
            c[n] = c[n]+i;
        };
    };
    if (c[0]>=60){
        c[1]=c[1]+Math.floor(c[0]/60);
        c[0]=c[0]+(c[0]%60 -c[0]);
    };
    if (c[1]>=60){
        c[2]=c[2]+Math.floor(c[1]/60);
        c[1]=c[1]+(c[1]%60 -c[1]);
    };
    if (c[2]>=24){
        c[3]=c[3]+Math.floor(c[2]/24);
        c[2]=c[2]+(c[2]%24 -c[2]);
    };
    return reversed(c);
};

let outp = [sumUnLists([0, 0, 0, 0], [0, 0, 0, 0]), 
                sumUnLists([1, 2, 0, 3], [1, 0, 2, 3]), 
                sumUnLists([70, 30, 0, 0], [0, 3240, 30, 0], [0, 0, 2345, 54]), 
                sumUnLists([3, 61, 75, 23])];

console.log(outp)

function testSumUnLists(){
    let outp = [sumUnLists([0, 0, 0, 0], [0, 0, 0, 0]), 
                sumUnLists([1, 2, 0, 3], [1, 0, 2, 3]), 
                sumUnLists([70, 30, 0, 0], [0, 3240, 30, 0], [0, 0, 2345, 54]), 
                sumUnLists([3, 61, 75, 23])];
    let answ = [];
    if (outp === answ){
        console.log("✅ testIsInt passed the test");
    } else {
        console.log("⛔️ testIsInt failed the test");
    };

};

function url_to_id(x) {
    return x.toString().slice(24).match("^playlist") && x.toString().slice(33).match("^list=") && x.toString().match("^https://www.youtube.com") && x.length === 72 ? x.toString().slice(-34) : "invalid url, not a youtube url or not a youtube playlist";
};

function display_text(){
    return "cool";
};


function test(){
    testIsInt();
    testIsFloat();
    testTimeParser();
    testSumUnLists();
};