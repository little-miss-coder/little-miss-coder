package com.example.farmanimals;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View.OnClickListener;
import android.widget.ImageButton;
import android.view.View;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {

//name buttons
    ImageButton cat;
    ImageButton dog;
    ImageButton sheep;
    ImageButton cow;
    ImageButton chicken;
    ImageButton duck;
    ImageButton horse;
    ImageButton pig;
    ImageButton bird;
    ImageButton barn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//define button names
        cat = (ImageButton) findViewById(R.id.imageButtonCat);
        dog = (ImageButton) findViewById(R.id.imageButtonDog);
        sheep = (ImageButton) findViewById(R.id.imageButtonSheep);
        cow = (ImageButton) findViewById(R.id.imageButtonCow);
        chicken = (ImageButton) findViewById(R.id.imageButtonChick);
        horse = (ImageButton) findViewById(R.id.imageButtonHorse);
        pig = (ImageButton) findViewById(R.id.imageButtonPig);
        duck = (ImageButton) findViewById(R.id.imageButtonDuck);
        bird = (ImageButton) findViewById(R.id.imageButtonBird);
        barn = (ImageButton) findViewById(R.id.imageButtonBarn);

//define sounds
        final MediaPlayer chickenNoise = MediaPlayer.create(this,R.raw.chickennoise);
        final MediaPlayer catNoise = MediaPlayer.create(this,R.raw.catnoise);
        final MediaPlayer cowNoise = MediaPlayer.create(this, R.raw.cownoise);
        final MediaPlayer dogNoise = MediaPlayer.create(this,R.raw.dognoise);
        final MediaPlayer duckNoise = MediaPlayer.create(this,R.raw.ducknoise);
        final MediaPlayer horseNoise = MediaPlayer.create(this,R.raw.horsenoise);
        final MediaPlayer pigNoise = MediaPlayer.create(this,R.raw.pignoise);
        final MediaPlayer sheepNoise = MediaPlayer.create(this,R.raw.sheepnoise);
        final MediaPlayer birdChirp = MediaPlayer.create(this,R.raw.birdchirp);

//chicken
        chicken.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "cluck", Toast.LENGTH_SHORT).show();
                         chickenNoise.start();
                     }
                 }
                );
//cat
        cat.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "meow", Toast.LENGTH_SHORT).show();
                         catNoise.start();
                     }
                 }
                );
//cow
        cow.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "moo", Toast.LENGTH_SHORT).show();
                         cowNoise.start();
                     }
                 }
                );
//dog
        dog.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "woof", Toast.LENGTH_SHORT).show();
                         dogNoise.start();
                     }
                 }
                );

//duck
        duck.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "quack", Toast.LENGTH_SHORT).show();
                         duckNoise.start();
                     }
                 }
                );

//horse
        horse.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "neigh", Toast.LENGTH_SHORT).show();
                         horseNoise.start();
                     }
                 }
                );

//pig
        pig.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "oink", Toast.LENGTH_SHORT).show();
                         pigNoise.start();
                     }
                 }
                );

//sheep
        sheep.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "bah", Toast.LENGTH_SHORT).show();
                         sheepNoise.start();
                     }
                 }
                );

//bird
        bird.setOnClickListener
                (new OnClickListener()
                 {
                     @Override
                     public void onClick(View view)
                     {
                         Toast.makeText(MainActivity.this, "chirp", Toast.LENGTH_SHORT).show();
                         birdChirp.start();
                     }
                 }
                );

//barn
        barn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {

                Intent activity2Intent = new Intent(getApplicationContext(), InsideBarn.class);
                startActivity(activity2Intent);
                Toast.makeText(MainActivity.this, "You've entered the barn", Toast.LENGTH_LONG).show();
            }
        });

    } //end on create



} //end main activity
