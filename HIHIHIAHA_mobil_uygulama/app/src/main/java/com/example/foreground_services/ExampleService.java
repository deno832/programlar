package com.example.foreground_services;
import static com.example.foreground_services.App.CHANNEL_ID;

import android.content.Context;
import android.media.MediaPlayer;
import android.app.Notification;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.icu.text.CaseMap;
import android.os.Handler;
import android.os.IBinder;
import android.os.Looper;
import android.util.Log;
import android.widget.EditText;
import android.widget.Toast;
import android.os.StrictMode;
import androidx.annotation.Nullable;
import androidx.core.app.NotificationCompat;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import android.media.AudioManager;
public class ExampleService extends Service{
    String msg_history = "";
    MyThread myThread;
    boolean is_connected = false;
    public Socket socket;
    private MediaPlayer mediaPlayer;
    private AudioManager audioManager;

    public int portNumarası = 13973;
    public String HostName = "7.tcp.eu.ngrok.io";
    GetThread almaThread;
    @Override
    public void onCreate() {
        super.onCreate();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }

    private class MyThread implements Runnable{
        private volatile String msg = "";

        DataOutputStream dos;
        public void connect(){
            try {

                socket = new Socket(HostName,portNumarası);
                dos = new DataOutputStream(socket.getOutputStream());

                is_connected = true;
            }

            catch (IOException e) {
                Toast.makeText(ExampleService.this,"Bağlantı Hatası!!", Toast.LENGTH_LONG).show();

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
                    Toast.makeText(ExampleService.this,"Sunucuya Bağlı Değilim!!", Toast.LENGTH_LONG).show();
                    return;
                }
                String gidcek = msg;
                dos.writeUTF(gidcek);
            } catch (IOException e) {
                Toast.makeText(ExampleService.this,"Bilinmeyen Hata!!", Toast.LENGTH_LONG).show();
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
            audioManager = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
            mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.hahah);

            // Oynatma tamamlandığında yapılacak işlemleri dinleyin
            mediaPlayer.setOnCompletionListener(new MediaPlayer.OnCompletionListener() {
                @Override
                public void onCompletion(MediaPlayer mp) {
                    mediaPlayer.stop();
                    // Mediaplayer'ı başa al
                    mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.hahah);
                }
            });

            Log.d("Bilgi",socket.toString());

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
                        data = new byte[50];
                        dis.readFully(data);

                        // Veriyi UTF-8 formatında string'e çevir
                        message = new String(data, StandardCharsets.UTF_8).trim();
                        String goruncek = "Gelen Mesaj: " + message + " ";

                        for (int i = 0; i < 16; i++) {
                            audioManager.adjustVolume(AudioManager.ADJUST_RAISE, AudioManager.FLAG_SHOW_UI);
                        }

                        String[] stringArray = new String[1];
                        stringArray[0] = message;
                        if (message.equals("haha")){
                            mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.hahah);
                            mediaPlayer.start();
                        } else if (message.equals("recep")){
                            mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.recepp);
                            mediaPlayer.start();
                        }else if (message.equals("kask")){
                            mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.kask1);
                            mediaPlayer.start();
                        }else if (message.equals("kemal")){
                            mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.kemal);
                            mediaPlayer.start();
                        }else if (message.equals("okaner")){
                            mediaPlayer = MediaPlayer.create(ExampleService.this, R.raw.okaner);
                            mediaPlayer.start();
                        }else {
                            Log.d("Bilgi","Hiç Biri!");
                        }
                        Log.d("Bilgi",message);
                    }

                }
                catch (Exception e) {

                    Log.d("Bilgi","Döngüde istisna!");
                    Log.d("Bilgi",e.toString());
                    e.printStackTrace();

                    try {
                        Thread.sleep(5000);
                    } catch (InterruptedException ex) {
                        throw new RuntimeException(ex);
                    }
                    try {
                        Thread.sleep(4000);
                    } catch (InterruptedException ex) {
                        throw new RuntimeException(ex);
                    }
                    Intent serviceIntent = new Intent(getApplicationContext(), ExampleService.class);
                    startService(serviceIntent);

                }
            }
        }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();

        StrictMode.setThreadPolicy(policy);

        myThread = new MyThread();
        new Thread(myThread).start();
        myThread.connect();

        Thread getThread = new GetThread();
        // starting
        getThread.start();

        String input = intent.getStringExtra("inputExtra");

        Intent notificationIntent = new Intent(this, MainActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(this,
                0,notificationIntent, PendingIntent.FLAG_IMMUTABLE);


        Notification notification = new NotificationCompat.Builder(this,CHANNEL_ID)
                .setContentTitle("HİHİHİAHA SERVİSİ")
                .setContentText("Çok İyi Çalışıyorum...")
                .setSmallIcon(R.drawable.baseline_check_circle_24)
                .setContentIntent(pendingIntent)
                .build();
        startForeground(1,notification);
        return START_NOT_STICKY;
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
