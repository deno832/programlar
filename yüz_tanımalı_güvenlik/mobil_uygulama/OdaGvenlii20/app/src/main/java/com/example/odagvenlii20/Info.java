package com.example.odagvenlii20;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class Info extends AppCompatActivity {

    public Socket socket;
    public String portNum;
    public String HostName;

    public String msg_history = "";
    MyThread myThread;
    boolean is_connected = false;


    public String nick;

    public int portNumarası;
    GetThread almaThread;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Intent intent = getIntent();


        portNum = intent.getStringExtra("portNum");
        HostName = intent.getStringExtra("ipAdrr");

        Log.d("Bilgi", portNum);
        Log.d("Bilgi", HostName);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        myThread = new MyThread();
        new Thread(myThread).start();
        myThread.connect();

        Thread getThread = new GetThread();
        // starting
        getThread.start();

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);

        myThread.sendMsgParam("al");
    }

    private class GetThread extends Thread{

        @Override
        public void run(){


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

                    data = new byte[100];
                    dis.readFully(data);

                    // Veriyi UTF-8 formatında string'e çevir
                    message = new String(data, StandardCharsets.UTF_8);

                    msg_history += message + "\n\n";
                    runOnUiThread(new Runnable() {
                        public void run() {
                            EditText history_box = findViewById(R.id.chat_history);
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

    private class MyThread implements Runnable{
        private volatile String msg = "";
        DataOutputStream dos;
        public void connect(){
            try {

                socket = new Socket(HostName,Integer.valueOf(portNum));
                dos = new DataOutputStream(socket.getOutputStream());

                Toast.makeText(Info.this,"Bağlantı Başarılı!!", Toast.LENGTH_LONG).show();
                is_connected = true;
            }

            catch (IOException e) {
                Toast.makeText(Info.this,"Bağlantı Hatası!!", Toast.LENGTH_LONG).show();

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
                    Toast.makeText(Info.this,"Sunucuya Bağlı Değilim!!", Toast.LENGTH_LONG).show();
                    return;
                }

                dos.writeUTF(msg);
            } catch (IOException e) {
                Toast.makeText(Info.this,"Bilinmeyen Hata!!", Toast.LENGTH_LONG).show();
            }
        }
        public void sendMsgParam(String msg){
            this.msg = msg;
            run();
        }
        public void start() {
        }
    }

    public void refresh_func(View v){
        EditText history_box = findViewById(R.id.chat_history);
        msg_history = "";
        history_box.setText(msg_history);

        myThread.sendMsgParam("al");
        Toast.makeText(this,"Loglar Yenilendi!", Toast.LENGTH_LONG).show();
    }

    public void clean_func(View v){
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("Bütün Loglar Silinecek! Emin Misiniz?")
                .setMessage("Bu İşlem Geri Alınamaz!")
                .setPositiveButton("Evet", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        myThread.sendMsgParam("sil");
                        Toast.makeText(Info.this,"Loglar Temizlendi! Yenileye Basınız!", Toast.LENGTH_LONG).show();
                    }
                })
                .setNegativeButton("Hayır", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        Toast.makeText(Info.this,"Loglar Temizlenmedi!", Toast.LENGTH_LONG).show();
                    }
                })
                .show();

    }
}