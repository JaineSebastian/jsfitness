package com.example.jsfitness;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class sendfeedback extends AppCompatActivity implements View.OnClickListener {
    EditText feedback;
    Button send;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sendfeedback);
        feedback = findViewById(R.id.editTextTextPersonName4);
        send = findViewById(R.id.button8);
        send.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        String feedback1 = feedback.getText().toString();
        if (feedback1.length() < 1) {
            feedback.setError("");
        } else {

            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

            String url = sh.getString("url", "") + "user_feedback";
            Toast.makeText(getApplicationContext(), url, Toast.LENGTH_SHORT).show();
            VolleyMultipartRequest volleyMultipartRequest;
            volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                    new Response.Listener<com.android.volley.NetworkResponse>() {
                        @Override
                        public void onResponse(NetworkResponse response) {
                            try {


                                JSONObject obj = new JSONObject(new String(response.data));

                                if (obj.getString("status").equals("ok")) {
                                    Toast.makeText(getApplicationContext(), " feedback send", Toast.LENGTH_SHORT).show();
//                                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//                                SharedPreferences.Editor ed = sh.edit();
//                                ed.putString("lid",obj.getString("lid"));
//                                ed.putString("uid", obj.getString("uid"));
//                                ed.commit();
                                    Intent i = new Intent(getApplicationContext(), user_home.class);
                                    startActivity(i);
                                } else {
                                    Toast.makeText(getApplicationContext(), "No user", Toast.LENGTH_SHORT).show();
                                }

                            } catch (JSONException e) {
                                e.printStackTrace();
                                Toast.makeText(getApplicationContext(), "----" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }) {

                @Override
                protected Map<String, String> getParams() throws AuthFailureError {
                    Map<String, String> params = new HashMap<>();
                    SharedPreferences o = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    params.put("uid", sh.getString("uid", ""));//passing to python
                    // Assuming params is a HashMap or similar data structure used to hold parameters
                    params.put("feedback", feedback1);


                    return params;
                }

                @Override
                protected Map<String, DataPart> getByteData() {
                    Map<String, DataPart> params = new HashMap<>();
                    long imagename = System.currentTimeMillis();
//                        params.put("image", new DataPart(imagename + ".png", getFileDataFromDrawable(bitmap)));
                    return params;
                }
            };

            Volley.newRequestQueue(this).add(volleyMultipartRequest);
        }
    }
}