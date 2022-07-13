function senduseDfL() {
    var u = document.getElementById("username");
    u = u.value;
    var p = document.getElementById("password");
    p = p.value;
    var data = new FormData();
    data.append("user", u);
    data.append("pas", p);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "log/log2");
    xhr.upload.addEventListener("progress", updateProgress, false);
    xhr.send(data);


}

function r() {
    $.get("/log/log3",
        function(response) {
            d(response);
        });


}

function d(r) {

    console.log(r.r);
    if (r.r == "done") {
        location.href = "rot";
    } else {
        location.href = "log/inerr";
    }

}


function updateProgress(evt) {
    if (evt.loaded == evt.total) alert("Okay");
    r();

}


function error() {
    alert("Pass ou username errado ou não resgistrado!")
}