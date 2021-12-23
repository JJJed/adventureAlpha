function openMapSpot(spot) {
    switch (spot):
        case 'forest':
            var server_data = [
                {"userID": usrID}
            ];

            $.ajax({
                url: "/render_forest",
                type: "POST",
                dataType: "json",
                data: JSON.stringify(server_data)
            });
}