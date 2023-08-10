package com.example.odagvenlii20;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SharedPreferences sharedPreferences = getSharedPreferences("MyPrefs", Context.MODE_PRIVATE);

        EditText portEntry = findViewById(R.id.port_entry);
        EditText ipEntry = findViewById(R.id.ip_entry);

        String gelen_port = sharedPreferences.getString("portNum", "8000");
        String gelen_ip = sharedPreferences.getString("ipAddr", "127.0.0.1");


        portEntry.setText(gelen_port);
        ipEntry.setText(gelen_ip);

    }

    public void Devam (View v){
        EditText portEntry = findViewById(R.id.port_entry);
        EditText ipEntry = findViewById(R.id.ip_entry);

        SharedPreferences sharedPreferences = getSharedPreferences("MyPrefs", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();

        String port = portEntry.getText().toString();


        String ip = ipEntry.getText().toString();

        Intent intent = new Intent(this, Info.class);

        editor.putString("portNum", port);
        editor.putString("ipAddr", ip);

        editor.apply();

        intent.putExtra("portNum", port);
        intent.putExtra("ipAdrr", ip);

        startActivity(intent);
    }
}