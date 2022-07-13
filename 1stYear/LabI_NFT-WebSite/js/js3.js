var i = 0;

function pic() {
    $.get("../us/showpic",
        function(response) {
            i++;
            var text = '<img src="../img/' + response.pics + '" width="500" height="600" type="submit"><input type="submit" onclick="add(id)" class="' + response.pics + '" id="h' + i + '" value="Add foto">';
            $("#dst").html(text);
            if (response.h != "-1") {

                pic2(response.h, text)
            }
        });

};

function pic2(d, text) {

    $.get("../us/showpic2", { i: d },
        function(response) {
            i++;

            var text2 = '<img src="../img/' + response.pics + '" width="500" height="600"><input onclick="add(id)" type="submit" class="' + response.pics + '" id="h' + i + '" value="Add foto">';
            text = text + text2;
            $("#dst").html(text);
            if (response.h != "-1") {

                pic2(response.h, text)
            }
        });

};

function add(id) {


    var u = document.getElementById(id);
    u = u.className;

    var data = new FormData();
    data.append("pic", u);
    var xhr = new XMLHttpRequest();

    xhr.open("POST", "../us/pictoadd");
    xhr.upload.addEventListener("progress", updateProgress, false);

    xhr.send(data);
    location.href = "../image/im2";

}

function updateProgress(evt) {
    if (evt.loaded == evt.total) alert("Okay");

}