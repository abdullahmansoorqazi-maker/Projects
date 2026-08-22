let shift = 3;


function changeShift(value){

shift += value;

document.getElementById("shift").innerText = shift;

}



function caesar(text, amount){


let result="";


for(let i=0;i<text.length;i++){


let char=text[i];


if(char.match(/[a-z]/i)){


let code=text.charCodeAt(i);


let base = code >=65 && code<=90 ? 65:97;


result += String.fromCharCode(
((code-base+amount)%26+26)%26+base
);


}

else{

result += char;

}

}


return result;

}





function encrypt(){

let text =
document.getElementById("input").value;


document.getElementById("output").value =
caesar(text,shift);

}



function decrypt(){

let text =
document.getElementById("input").value;


document.getElementById("output").value =
caesar(text,-shift);

}