function checkReg() {

    var name = userName.html();
    var tag = userTag.html();
    var passwd = userPswd.html();

    var server_data = [
        {"name": name},
        {"tag": tag},
        {"passwd": passwd}
    ];

    $.ajax({
        url: "/reg_check",
        type: "POST",
        dataType: "json",
        data: JSON.stringify(server_data),
        success: function(data) {
            stat = getInt(data);
        }
    });
    if (stat == 0) {
        $("#RNope").html("Sorry that Username/Tag combination is already taken!");
    } else if (stat == 1) {
        $("#RNope").html("");
        var login_link = document.createElement("A");
        login_link.innerHTML = "LOGIN HERE!";
        login_link.href = "https://adventuregame.jeddev.net/login";
        document.body.appendChild(login_link);
    }

}