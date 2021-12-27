function checkLog() {

    var name = userNAME.html();
    var tag = userTAG.html();
    var passwd = userPSWD.html();

    var server_data = [
        {"name": name},
        {"tag": tag},
        {"passwd": passwd}
    ];

    $.ajax({
        url: "/log_check",
        type: "POST",
        dataType: "json",
        data: JSON.stringify(server_data),
        success: function(data) {
            stat = getInt(data);
        }
    });
    if (stat == 0) {
        $("#LNope").html("Sorry that Username/Tag combination is already taken!");
    }
}