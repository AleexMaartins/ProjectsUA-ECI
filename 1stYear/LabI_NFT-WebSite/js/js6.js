var img2;



function updatePhoto2(event) {

    var reader = new FileReader();
    reader = iml2(event);


    img2 = event.target.files[0];
    //Libertar recursos da imagem selecionada

}

function iml2(event) {
    //Criar uma imagem
    var img = new Image();
    img = im2(img);

}

function im2(img) {
    canvas = document.getElementById("photo2");
    ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0, img.width, img.height, 0, 0, 530, 400);

}




function sendFile() {
    var data = new FormData();
    data.append("i2", img2);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "../image/done2");
    xhr.upload.addEventListener("progress", updateProgress, false);
    xhr.send(data);
}





function updateProgress(evt) {
    if (evt.loaded == evt.total) alert("Okay");
    location.href = "../rot"
}