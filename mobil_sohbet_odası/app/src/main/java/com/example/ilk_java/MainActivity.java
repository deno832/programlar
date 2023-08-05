package com.example.ilk_java;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void devam_func(View v){
        EditText t = findViewById(R.id.nick_entry);
        String nick = t.getText().toString();

        EditText portEntry = findViewById(R.id.port_entry);
        int port = Integer.valueOf(portEntry.getText().toString());

        EditText ipEntry = findViewById(R.id.ip_entry);
        String ip = ipEntry.getText().toString();

        Intent intent = new Intent(this, ChatActivity.class);
        intent.putExtra("veriAnahtari", nick);
        intent.putExtra("portNum", port);
        intent.putExtra("ipAdrr", ip);


        startActivity(intent);

    }
}