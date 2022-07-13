function senduseD() {
    var u = document.getElementById("username");
    u = u.value;
    var p = document.getElementById("password");
    p = p.value;

    $.get("/log/cre", { user: u, pas: p },
        function(response) {

            if (response.s == "s") {
                location.href = "../rot"
            } else {
                alert("Nome de usario já em uso")
            }
        });


}