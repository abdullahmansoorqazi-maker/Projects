function decodeMessage(){

    let file = document.getElementById("imageInput").files[0];

    if(!file){
        alert("Select image");
        return;
    }

    let reader = new FileReader();

    reader.onload = function(event){

        let img = new Image();

        img.onload = function(){

            let canvas = document.getElementById("canvas");
            let ctx = canvas.getContext("2d");

            canvas.width = img.width;
            canvas.height = img.height;

            ctx.drawImage(img,0,0);

            let data = ctx.getImageData(0,0,canvas.width,canvas.height).data;

            let binaryMessage="";
            let message="";

            for(let i=0;i<data.length;i+=4){

                binaryMessage += (data[i] & 1);

                if(binaryMessage.length % 8 === 0){

                    let char = String.fromCharCode(
                        parseInt(binaryMessage.slice(-8),2)
                    );

                    if(char === "\0") break;

                    message += char;
                }
            }

            document.getElementById("output").innerText = message;
        }

        img.src = event.target.result;
    }

    reader.readAsDataURL(file);
}