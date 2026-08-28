package com.example.jsfitness;

//import androidx.appcompat.app.AppCompatActivity;
//
//import android.os.Bundle;
//
//public class custom_view_workout extends AppCompatActivity {
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.custom_view_workout);
//    }
//}

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
//import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.squareup.picasso.Picasso;

public class custom_view_workout extends BaseAdapter implements View.OnClickListener {
    String[] uid,name,desc;
    private Context context;
    ImageView img;
    String[] urll;
    Button trainer;

    public custom_view_workout(Context applicationContext, String[] uid, String[] name,String[] urll, String[] desc) {
        this.context = applicationContext;
        this.uid = uid;
        this.name = name;
        this.desc = desc;


        this.urll = urll;

    }


    @Override
    public int getCount() {
        return name.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.custom_view_workout,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        img = (ImageView)gridView.findViewById(R.id.imageView3);
        TextView tv1=(TextView)gridView.findViewById(R.id.textView25 );
        TextView tv2=(TextView)gridView.findViewById(R.id.textDescriptionView26 );
//        TextView tv3=(TextView)gridView.findViewById(R.id.textView15);
//        TextView tv4=(TextView)gridView.findViewById(R.id.textView11);
//        TextView tv5=(TextView)gridView.findViewById(R.id.textView8);
//        TextView tv6=(TextView)gridView.findViewById(R.id.textView10);


//        Button tv8=(Button)gridView.findViewById(R.id.button6);
//        tv8.setTag(id[i]);
//        tv8.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
//                SharedPreferences.Editor ed = sh.edit();
//                ed.putString("eqpt_id",view.getTag().toString());
//                ed.commit();
//                Intent i = new Intent(context,booking.class);
//                i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//                context.startActivity(i);
//            }
//        });





        tv1.setTextColor(Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);//color setting
//        tv3.setTextColor(Color.BLACK);
//        tv4.setTextColor(Color.BLACK);
//        tv5.setTextColor(Color.BLACK);
//        tv6.setTextColor(Color.BLACK);




        tv1.setText(name[i]);
        tv2.setText(desc[i]);
//        tv3.setText(phone[i]);






        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context.getApplicationContext());
        String imgUrl = sh.getString("imgurl","")+urll[i];
        Log.d("imgggggggggggggggg",imgUrl);
        Toast.makeText(context,imgUrl,Toast.LENGTH_LONG).show();
//        Picasso.with(context).load(imgUrl).into(img);

        Glide.with(context).asGif().load(imgUrl).into(img);



        return gridView;

    }


    @Override
    public void onClick(View view) {
//        Intent intent = new Intent(context, view_catergory.class);
//        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//        context.startActivity(intent);
    }
}