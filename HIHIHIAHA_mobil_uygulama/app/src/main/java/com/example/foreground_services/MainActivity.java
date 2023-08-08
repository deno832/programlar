package com.example.foreground_services;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    private EditText editTextInput;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    public void startService(View v){

        Intent serviceIntent = new Intent(this,ExampleService.class);
        serviceIntent.putExtra("inputExtra","input");
        startForegroundService(serviceIntent);

    }

    public void stopService(View v){

        Intent serviceIntent = new Intent(this,ExampleService.class);

        stopService(serviceIntent);
    }
}