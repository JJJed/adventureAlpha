function RNope(x) {
    if(x == 1) {
        document.getElementById("RNope").innerHTML = "";
    }
    else if(x == 0) {
        document.getElementById("RNope").innerHTML = "Sorry that Username/Tag combination is already taken!";
    }
}