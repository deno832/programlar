This project uses a Raspberry Pi and a camera to monitor the door of a room. Each time someone approaches, it attempts to recognize their face. If it can recognize the face, it saves the name along with the date and time to an SQLite file. If it cannot recognize the face, it saves it as 'unknown' with the same details. A socket server within the same code listens for and accepts connections. If the server receives a 'get' message from the client, it sends the database to that client. As the client, I developed a mobile application using Java in Android Studio. The mobile app saves the last entered port and IP address using SharedPreferences and automatically fills them in the input fields for future use.


![uygulama2](https://github.com/deno832/programlar/assets/94462464/258bb056-1343-404a-810a-e1eec857fa42)


![uygulama1](https://github.com/deno832/programlar/assets/94462464/48538f51-b9de-4cf2-a4a6-22d78b565f29)
