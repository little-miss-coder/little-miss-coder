package com.example.farmanimals;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ImageButton;
import android.view.View;
import android.widget.Toast;

import android.os.Bundle;

public class InsideBarn extends AppCompatActivity {

    ImageButton sleepingdog;
    Button buttonoutside;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inside_barn);

        sleepingdog = (ImageButton) findViewById(R.id.imageButtonDogInside);
        buttonoutside = (Button) findViewById(R.id.buttonToOutside);
        final MediaPlayer dogNoise = MediaPlayer.create(this,R.raw.dognoise);

        sleepingdog.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(InsideBarn.this, "You woke the dog!", Toast.LENGTH_SHORT).show();
                         dogNoise.start();
                     }
                 }
                );
        buttonoutside.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {

                Intent activity2Main = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(activity2Main);
                Toast.makeText(InsideBarn.this, "You Went Back Outside", Toast.LENGTH_LONG).show();
            }
        });

    }
}
