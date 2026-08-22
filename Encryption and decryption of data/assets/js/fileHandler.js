function encryptFile(){

let file =
document.getElementById("fileInput").files[0];


if(!file){
alert("Select file");
return;
}


// only text files

if(file.type !== "text/plain"){

alert(
"Currently Caesar File Cipher supports TXT files only. PDF/DOCX will use separate handler."
);

return;

}



let shift =
parseInt(
document.getElementById("fileShift").value
);



let reader =
new FileReader();



reader.onload=function(e){


let text=e.target.result;


let result="";


for(let i=0;i<text.length;i++){


let code=text.charCodeAt(i);


result +=
String.fromCharCode(code+shift);


}



downloadFile(
result,
"encrypted_"+file.name
);


}



reader.readAsText(file);


}





function decryptFile(){


let file =
document.getElementById("fileInput").files[0];


let shift =
parseInt(
document.getElementById("fileShift").value
);



let reader =
new FileReader();



reader.onload=function(e){


let text=e.target.result;


let result="";


for(let i=0;i<text.length;i++){


let code=text.charCodeAt(i);


result +=
String.fromCharCode(code-shift);


}



downloadFile(
result,
"decrypted_"+file.name
);


}



reader.readAsText(file);


}





function downloadFile(data,name){


let blob =
new Blob(
[data],
{
type:"text/plain"
}
);



let a=document.createElement("a");


a.href=
URL.createObjectURL(blob);


a.download=name;


a.click();

}