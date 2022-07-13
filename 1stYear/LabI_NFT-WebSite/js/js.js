var im1;
var im2;

function updatePhoto(event) {


    var reader = new FileReader();
    reader = iml1(event);


    im1 = event.target.files[0];
    //Libertar recursos da imagem selecionada


}

function iml1(event) {
    //Criar uma imagem
    var img = new Image();
    img = im1(img);

}

function im1(img) {
    canvas = document.getElementById("photo1");
    ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0, img.width, img.height, 0, 0, 530, 400);


}

function updatePhoto2(event) {

    var reader = new FileReader();
    reader = iml2(event);


    im2 = event.target.files[0];
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
    data.append("i1", im1);
    data.append("i2", im2);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "done");
    xhr.upload.addEventListener("progress", updateProgress, false);
    xhr.send(data);
    r()
}





function updateProgress(evt) {
    if (evt.loaded == evt.total) alert("Okay");
}

function r() {
    var t = 1;
    if (t == 1) {
        location.href = "../rot"
    }
}