let encodedImageData;



function encodeImage(){


let file =
document.getElementById("imageInput").files[0];


let message =
document.getElementById("secretText").value;



let reader=new FileReader();


reader.onload=function(e){


let img=new Image();


img.onload=function(){


let canvas =
document.getElementById("canvas");


let ctx =
canvas.getContext("2d");


canvas.width=img.width;
canvas.height=img.height;


ctx.drawImage(img,0,0);



let data =
ctx.getImageData(
0,
0,
canvas.width,
canvas.height
);



let binary =
message.split("")
.map(c =>
c.charCodeAt(0)
.toString(2)
.padStart(8,'0')
)
.join("")
+
"00000000";



for(let i=0;i<binary.length;i++){


data.data[i*4] =
(data.data[i*4]&254)
|
Number(binary[i]);


}



ctx.putImageData(data,0,0);



let link =
document.createElement("a");


link.download="encoded.png";


link.href =
canvas.toDataURL();


link.click();



alert("Message Hidden");


}



img.src=e.target.result;


}



reader.readAsDataURL(file);


}







function decodeImage(){


let file =
document.getElementById("imageInput").files[0];


let reader=new FileReader();


reader.onload=function(e){


let img=new Image();


img.onload=function(){


let canvas =
document.getElementById("canvas");


let ctx =
canvas.getContext("2d");


canvas.width=img.width;
canvas.height=img.height;


ctx.drawImage(img,0,0);



let data =
ctx.getImageData(
0,
0,
canvas.width,
canvas.height
);



let bits="";


for(let i=0;i<data.data.length;i+=4){


bits +=
(data.data[i]&1);


}



let chars=[];


for(let i=0;i<bits.length;i+=8){


let byte =
bits.substring(i,i+8);



if(byte==="00000000")
break;



chars.push(
String.fromCharCode(
parseInt(byte,2)
)
);



}



document.getElementById("decoded").innerText =
chars.join("");

}



img.src=e.target.result;


}



reader.readAsDataURL(file);


}