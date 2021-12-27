var usrID;

function getID(id) {
    usrID = id;
    usrID = getInt(usrID);
}

var currentSize;
$("#chop").hide();

function selectTreeSize(size) {
    if (size == 0) {
        $.ajax({
            url: "/tree1",
            type: "POST",
            dataType: "json",
            success: function(data) {
                $("#size").html("Small")
                var currentSize = getInt(data);
                tree(currentSize);
            }
        });
    } else if (size == 1) {
        $.ajax({
            url: "/tree2",
            type: "POST",
            dataType: "json",
            success: function(data) {
                $("#size").html("Medium")
                var currentSize = getInt(data);
                tree(currentSize);
            }
        });
    } else if (size == 2) {
        $.ajax({
            url: "/tree3",
            type: "POST",
            dataType: "json",
            success: function(data) {
                $("#size").html("Large")
                var currentSize = getInt(data);
                tree(currentSize);
            }
        });
    }
}

function tree(size) {
    switch (size) {
        case 0:
            $("#currentHitsLeft").html("10")
            $("#maxHits").html("10")
            $("#bar").max = 10;
            $("#bar").value = 10;
            break;
        case 1:
            $("#currentHitsLeft").html("100")
            $("#maxHits").html("100")
            $("#bar").max = 100;
            $("#bar").value = 100;
            break;
        case 2:
            $("#currentHitsLeft").html("1000")
            $("#maxHits").html("1000")
            $("#bar").max = 1000;
            $("#bar").value = 1000;
            break;
    }
    $("#selectSize").hide();
    $("#chop").show();
}

function chop() {
    var max = $("#bar").max;
    var left = $("#bar").value;
    var stat;

    var server_data = [
        {"maxHits": max},
        {"hitsLeft": left},
        {"userID": usrID}
    ];

    $.ajax({
        url: "/tree4",
        type: "POST",
        dataType: "json",
        data: JSON.stringify(server_data),
        success: function(data) {
            var stat = getInt(data);
        }
    });

    var hitsInt = getInt($("#currentHitsLeft").html());
    var newHits = hitsInt - stat;
    $("#currentHitsLeft").html(newHits)
    $("#bar").value = hitsInt - newHits;
}