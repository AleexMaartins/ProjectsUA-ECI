var k = 0;

function pic() {

    $.get("../showim",
        function(response) {
            k++;

            console.log(response.pics)
            var text = '<div class="row text-center"><div class="col-lg-4"><a href="javascript:void(0)" class="card border-0 text-dark"><img class="card-img-top" src="img/' + response.pic + '" alt=><span class="card-body"><h4 class="' + response.u + '" id="h' + k + '">Coleção de ' + response.u + ' </h4><input id="h' + k + '" type="submit" value="Click here to see collection" onclick="showpic(id)"></span></a></div>';
            $("#dst").html(text);
            if (response.h != "-1") {

                pic2(response.h, text)
            }
        });

};

function pic2(d, text) {

    $.get("../showim2", { i: d },
        function(response) {
            k++;

            console.log(response.pics)
            var text2 = '<div class="row text-center"><div class="col-lg-4"><a href="javascript:void(0)" class="card border-0 text-dark"><img class="card-img-top" src="img/' + response.pic + '" alt=><span class="card-body"><h4 class="' + response.u + '" id="h' + k + '">Coleção de ' + response.u + ' </h4><input type="submit" id="h' + k + '"  value="Click here to see collection" onclick="showpic(id)"></span></a></div>';
            text = text2 + text
            $("#dst").html(text);
            if (response.h != "-1") {
                pic2(response.h, text)
            }
        });

};

function showpic(id) {

    var u = document.getElementById(id);
    u = u.className;

    var data = new FormData();
    data.append("user", u);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "../us/show");
    xhr.upload.addEventListener("progress", updateProgress, false);

    xhr.send(data);
    location.href = "../us/usepic";

}

function updateProgress(evt) {
    if (evt.loaded == evt.total) alert("Okay");

}

function logO() {

    $.get("../log/logoff",
        function() {
            location.href = "../"
        });


}