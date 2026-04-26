function encodeMessage(){

    let file = document.getElementById("imageInput").files[0];
    let message = document.getElementById("message").value;

    if(!file || message === ""){
        alert("Select image and enter message");
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

            let imageData = ctx.getImageData(0,0,canvas.width,canvas.height);
            let data = imageData.data;

            let binaryMessage="";

            for(let i=0;i<message.length;i++){
                binaryMessage += message[i]
                .charCodeAt(0)
                .toString(2)
                .padStart(8,'0');
            }

            binaryMessage += "00000000";

            let index=0;

            for(let i=0;i<data.length && index<binaryMessage.length;i+=4){
                data[i] = (data[i] & 254) | parseInt(binaryMessage[index]);
                index++;
            }

            ctx.putImageData(imageData,0,0);

            let link=document.createElement("a");
            link.download="encoded.png";
            link.href=canvas.toDataURL();
            link.click();
        }

        img.src=event.target.result;
    }

    reader.readAsDataURL(file);
}