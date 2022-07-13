var i = 0;

function pic() {

    $.get("../us/showpic3",
        function(response) {
            i++;
            var text = '<img src="../img/' + response.pics + '" width="500" height="600" type="submit">';
            $("#dst").html(text);
            if (response.h != "-1") {

                pic2(response.h, text)
            }
        });

};

function pic2(d, text) {

    $.get("../us/showpic4", { i: d },
        function(response) {
            i++;

            var text2 = '<img src="../img/' + response.pics + '" width="500" height="600">';
            text = text + text2;
            $("#dst").html(text);
            if (response.h != "-1") {

                pic2(response.h, text)
            }
        });

};



function updateProgress(evt) {
    if (evt.loaded == evt.total) alert("Okay");

}