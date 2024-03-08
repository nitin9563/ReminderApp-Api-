# This is an API for reminder app


<h3>End-points for data are: </h3> 
1. <b>GET</b> /info/ -: <br>

        Send this end-point with get request to get all the saved reminders

2. <b>POST</b> /info/  -: <br>

        send post request with json body 
        {
            "date": "2024-03-12",
            "time": "20:20:00",
            "msg": "Remind me this msg"
        }
        it will save the reminder in table name "ReminderInfo" in database 
