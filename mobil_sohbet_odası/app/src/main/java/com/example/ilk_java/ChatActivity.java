package com.example.ilk_java;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import android.content.Intent;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class ChatActivity extends AppCompatActivity {
    String msg_history = "";
    MyThread myThread;
    boolean is_connected = false;
    public Socket socket;

    public String nick;

    public int portNumarası;
    public String HostName;
    GetThread almaThread;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);

        Intent intent = getIntent();
        nick = intent.getStringExtra("veriAnahtari");
        portNumarası = intent.getIntExtra("portNum",0);
        HostName = intent.getStringExtra("ipAdrr");

        Log.d("Bilgi",nick);

        // Alınan veriyi kullanın

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        myThread = new MyThread();
        new Thread(myThread).start();
        myThread.connect();

        Thread getThread = new GetThread();
        // starting
        getThread.start();

        /*GetThread getThread = new GetThread();
        new Thread(getThread).start();

        getThread.run();*/

    }

    private class MyThread implements Runnable{
        private volatile String msg = "";

        DataOutputStream dos;
        public void connect(){
            try {

                socket = new Socket(HostName,portNumarası);
                dos = new DataOutputStream(socket.getOutputStream());

                Toast.makeText(ChatActivity.this,"Bağlantı Başarılı!!", Toast.LENGTH_LONG).show();
                is_connected = true;
            }

            catch (IOException e) {
                Toast.makeText(ChatActivity.this,"Bağlantı Hatası!!", Toast.LENGTH_LONG).show();

                e.printStackTrace();
            }
        }

        @Override
        public void run(){
            try {
                if (msg == ""){
                    return;
                }
                if (!is_connected){
                    Toast.makeText(ChatActivity.this,"Sunucuya Bağlı Değilim!!", Toast.LENGTH_LONG).show();
                    return;
                }
                String gidcek = nick + "----> " + msg;
                dos.writeUTF(gidcek);
            } catch (IOException e) {
                Toast.makeText(ChatActivity.this,"Bilinmeyen Hata!!", Toast.LENGTH_LONG).show();
            }
        }
        public void sendMsgParam(String msg){
            this.msg = msg;
            run();
        }

        public void start() {
        }
    }

    private class GetThread extends Thread{

        @Override
        public void run(){
            EditText history_box = findViewById(R.id.chat_history);
            Log.d("Bilgi",socket.toString());

            try {
                DataInputStream dis = new DataInputStream(socket.getInputStream());
            } catch (IOException e) {
                e.printStackTrace();
            }

            int dataSize;
            byte[] data;
            String message;
            DataInputStream dis = null;
            try {
                dis = new DataInputStream(socket.getInputStream());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

            try {
                while (true){
                    //dataSize = dis.readInt();
                    //Log.d("Bilgi", "Data size: " + dataSize);
                    // Veriyi al

                    data = new byte[50];
                    dis.readFully(data);

                    // Veriyi UTF-8 formatında string'e çevir
                    message = new String(data, StandardCharsets.UTF_8);

                    msg_history += message + "\n\n";
                    runOnUiThread(new Runnable() {
                        public void run() {
                            // UI thread üzerinde yapılacak işlemler burada yapılır
                            // Örneğin, bir TextView'in metnini güncelleme gibi
                            history_box.setText(msg_history);
                        }
                    });
                    //history_box.setText(msg_history);
                    Log.d("Bilgi",message);
                }

            } catch (Exception e) {
                Log.d("Bilgi","Döngüde istisna!");
                e.printStackTrace();
            }
        }

    }
    public void basma(View v){
        EditText history_box = findViewById(R.id.chat_history);
        EditText t = findViewById(R.id.entry);
        String msgs = t.getText().toString();
        t.setText("");
        msg_history += "Sen ----> " + msgs + "\n\n";
        history_box.setText(msg_history);
        myThread.sendMsgParam(msgs);
    }
}