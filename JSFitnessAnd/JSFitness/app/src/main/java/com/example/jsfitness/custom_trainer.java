package com.example.jsfitness;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
//import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

public class custom_trainer extends BaseAdapter implements View.OnClickListener {
    String[] id,uid,name,email,phone;
    private Context context;
    ImageView im;
    String[] urll;
    Button trainer;

    public custom_trainer(Context applicationContext, String[] uid, String[] name, String[] email, String[] phone,String[] urll, String[] id) {
        this.context = applicationContext;
        this.id = id;
        this.uid = uid;
        this.name = name;
        this.email = email;
        this.phone = phone;
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
            gridView=inflator.inflate(R.layout.activity_custom_trainer,null);//same class name

        }
        else
        {
            gridView=(View)view;

        }
        im = (ImageView)gridView.findViewById(R.id.imageView);
        TextView tv1=(TextView)gridView.findViewById(R.id.textView7 );
        TextView tv2=(TextView)gridView.findViewById(R.id.textView11 );
        TextView tv3=(TextView)gridView.findViewById(R.id.textView15);
//        TextView tv4=(TextView)gridView.findViewById(R.id.textView11);
//        TextView tv5=(TextView)gridView.findViewById(R.id.textView8);
//        TextView tv6=(TextView)gridView.findViewById(R.id.textView10);


        Button tv8=(Button)gridView.findViewById(R.id.button5);
        tv8.setTag(id[i]);
        tv8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor ed = sh.edit();
                ed.putString("t_id",view.getTag().toString());
                ed.commit();
                Intent i = new Intent(context,view_catergory.class);
                i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(i);

            }
        });





        tv1.setTextColor(Color.BLACK);//color setting
        tv2.setTextColor(Color.BLACK);//color setting
        tv3.setTextColor(Color.BLACK);
//        tv4.setTextColor(Color.BLACK);
//        tv5.setTextColor(Color.BLACK);
//        tv6.setTextColor(Color.BLACK);




        tv1.setText(name[i]);
        tv2.setText(email[i]);
        tv3.setText(phone[i]);






        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context.getApplicationContext());
        String imgUrl = sh.getString("imgurl","")+urll[i];
        Log.d("imgggggggggggggggg",imgUrl);
        Toast.makeText(context,imgUrl,Toast.LENGTH_LONG).show();
        Picasso.with(context).load(imgUrl).into(im);





        return gridView;

    }


    @Override
    public void onClick(View view) {
        Intent intent = new Intent(context, view_catergory.class);
        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        context.startActivity(intent);
    }
}
