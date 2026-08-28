package com.example.jsfitness;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.provider.MediaStore;
import android.provider.Settings;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class signup extends AppCompatActivity implements View.OnClickListener {
    final int CAMERA_PIC_REQUEST = 0, GALLERY_CODE = 201;
    private Uri mImageCaptureUri;
    public static String encodedImage = "", path = "";
    public static byte[] byteArray;
    Bitmap bitmap = null;

    EditText n_id, ph_id, em_id, weight, height, u_id, p_id;
    Spinner dis;
    Button bt2;
    ImageView img;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        n_id = findViewById(R.id.editTextTextPersonName3);
        ph_id = findViewById(R.id.editTextPhone);
        em_id = findViewById(R.id.editTextTextEmailAddress);
        weight = findViewById(R.id.editTextTextPersonWeightName);
        height = findViewById(R.id.editTextTextPersonHeightName4);
        u_id = findViewById(R.id.editTextTextPersonName6);
        p_id = findViewById(R.id.editTextTextPassword2);

        bt2 = findViewById(R.id.button3);

        bt2.setOnClickListener(this);

//
//        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && ContextCompat.checkSelfPermission(this,
//                Manifest.permission.READ_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
//            Intent intent = new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
//                    Uri.parse("package:" + getPackageName()));
//            finish();
//            startActivity(intent);
//            return;
//        }
    }

    @Override
    public void onClick(View view) {
        String name = n_id.getText().toString();
        String phone = ph_id.getText().toString();
        String email = em_id.getText().toString();
        String weight1 = weight.getText().toString();
        String height1 = height.getText().toString();
        String username = u_id.getText().toString();
        String password = p_id.getText().toString();

        if (name.length() < 1) {
            n_id.setError("Name cannot be empty");
        } else if (phone.length() < 1) {
            ph_id.setError("Phone cannot be empty");
        } else if (email.length() < 1) {
            em_id.setError("Email cannot be empty");
        } else if (weight1.length() < 1) {
            weight.setError("Weight cannot be empty");
        } else if (height1.length() < 1) {
            height.setError("Height cannot be empty");
        } else if (username.length() < 1) {
            u_id.setError("Username cannot be empty");
        } else if (password.length() < 1) {
            p_id.setError("Password cannot be empty");
        } else {
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String url = sh.getString("url", "") + "user_registration";
            Toast.makeText(getApplicationContext(), url, Toast.LENGTH_SHORT).show();
            VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                    new Response.Listener<NetworkResponse>() {
                        @Override
                        public void onResponse(NetworkResponse response) {
                            try {
                                JSONObject obj = new JSONObject(new String(response.data));
                                if (obj.getString("status").equals("ok")) {
                                    Toast.makeText(getApplicationContext(), "Registration success", Toast.LENGTH_SHORT).show();
                                    Intent i = new Intent(getApplicationContext(), login.class);
                                    startActivity(i);
                                } else {
                                    Toast.makeText(getApplicationContext(), "Registration failed", Toast.LENGTH_SHORT).show();
                                }
                            } catch (JSONException e) {
                                e.printStackTrace();
                                Toast.makeText(getApplicationContext(), "Error: " + e.getMessage(), Toast.LENGTH_SHORT).show();
                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(getApplicationContext(), "Error: " + error.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }) {
                @Override
                protected Map<String, String> getParams() throws AuthFailureError {
                    Map<String, String> params = new HashMap<>();
                    SharedPreferences o = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    params.put("uid", sh.getString("uid",""));//passing to python
                    params.put("name", name);
                    params.put("phone", phone);
                    params.put("email", email);
                    params.put("username", username);
                    params.put("password", password);
                    params.put("weight", weight1);
                    params.put("height", height1);
                    return params;
                }

//                    @Override
//                    protected Map<String, DataPart> getByteData() {
//                        Map<String, DataPart> params = new HashMap<>();
//                        if (bitmap != null) {
//                            long imagename = System.currentTimeMillis();
//                            params.put("image", new DataPart(imagename + ".png", getFileDataFromDrawable(bitmap)));
//                        }
//                        return params;
//                    }
            };
            Volley.newRequestQueue(this).add(volleyMultipartRequest);
        }
    }}





