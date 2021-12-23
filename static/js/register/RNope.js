function RNope(x) {
    if(x == 1) {
        $("#LNope").html("");
    }
    else if(x == 0) {
        $("#LNope").html("Sorry that Username/Tag combination is already taken!");
    }
}