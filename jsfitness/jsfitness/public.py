import uuid
from flask import *
from database import *
from flask import jsonify

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def public_home():
    return render_template('public/public_home.html')


@public.route('/login',methods=['get','post'])
def login_all():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        qa="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(qa)
        if res:
            session['lid']=res[0]['login_id']
            if res[0]['usertype']=='admin':
                # return redirect(url_for('admin.admin_home'))
                 return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: red;"></h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_home';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
            elif res[0]['usertype']=='trainer':
                    qa="SELECT * FROM trainer WHERE login_id='%s'"%(session['lid'])
                    q=select(qa)
                    if q:
                        session['tid']=q[0]['trainer_id']
                        return """
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
                                <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
                                <h3 style="color: red;"></h3>
                            </div>
                            <script>
                                setTimeout(function() {
                                    window.location.href = 'trainer_home';
                                }, 4000); // Redirect after 2 seconds
                           </script>
                        """

        else:
            # return """<script>alert('Inalid username and password');window.location='login';</script>"""
                             return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/inavlid.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: red;">Invalid username and password....!</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/login';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
            
    
    return  render_template('public/login.html')

# ----------------------------------------------andriod--------------------------------

@public.route('/user_registration',methods = ['post','get'])
def user_registration():
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    weight = request.form['weight']
    height = request.form['height'] 
    q = "insert into login values(NULL,'%s','%s','user')"%(username,password)
    m = insert(q)
    q1 = "insert into user values(NULL,'%s','%s','%s','%s','%s','%s')"%(m,name,phone,email,weight,height)
    insert(q1)
    return jsonify(status ="ok")

@public.route('/userlogin',methods=['post','get'])
def login():
    username = request.form['username']
    password = request.form['password']
    q = "select * from login where username = '%s' and password = '%s'"%(username,password)
    res = select(q)
    if res:
        if res[0]['usertype']=='user':
            login_id = res[0]['login_id']
            q = "select * from user where login_id ='%s'"%(login_id)
            result = select(q)
            if result:
                user_id = result[0]['user_id']
                return jsonify(status="ok",lid=login_id,uid=user_id)
            else:
                return jsonify(status ="no")                
    else:
        return jsonify(status ="no")