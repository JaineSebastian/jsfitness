import uuid
from flask import *
from database import *
from flask import jsonify

admin=Blueprint('admin',__name__)


@admin.route('/admin_home',methods=['get','post'])
def admin_home():
    return render_template('admin/admin_home.html')

@admin.route('/manage_category',methods=['get','post'])
def admin_manage_category():
     data={}
     q = "select * from category"
     data['cat']=select(q)

     if 'submit' in request.form:
        category_name=request.form['category']
        m="insert into category values(Null,'%s')"%(category_name)
        insert(m)
      #   return """<script>alert('added successfull');window.location='manage_category';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: red;"></h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_category';
        }, 4000); // Redirect after 2 seconds
    </script>
"""


     if 'action' in request.args:
        action=request.args['action']
        catgory_id=request.args['catgory_id']
     else:
        action=None
    
    
     if action=='update':
        fu="select * from category where catgory_id='%s'"%(catgory_id)
        data['updates']=select(fu)
     
     if 'update' in request.form:
        category_name=request.form['category']
        yy="update category set category_name='%s' where catgory_id='%s'"%(category_name,catgory_id)
        update(yy)
      #   return """<script>alert('updated successfull');window.location='manage_category';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">UPDATED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_category';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
     
     if action=='delete':
        pu="delete from category where catgory_id='%s'"%(catgory_id)
        delete(pu)
      #   return """<script>alert('deleted successfull');window.location='manage_category';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">DELETED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_category';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
     return render_template('admin/manage_category.html',data=data)






@admin.route('/manage_timeslots',methods=['get','post'])
def admin_manage_timeslots():
     data={}
     q = "select * from timeslots"
     data['time']=select(q)
     if 'submit' in request.form:
        date=request.form['date']
        from_time=request.form['from_time']
        to_time=request.form['to_time']
        m="insert into timeslots values(Null,'%s','%s','%s')"%(date,from_time,to_time)
        insert(m)
     if 'action' in request.args:
        action=request.args['action']
        time_slot_id=request.args['time_slot_id']
     else:
        action=None
    
    
     if action=='update':
        fu="select * from timeslots where time_slot_id='%s'"%(time_slot_id)
        data['updates']=select(fu)
     
     if 'update' in request.form:
        date=request.form['date']
        from_time=request.form['from_time']
        to_time=request.form['to_time']
        yy="update timeslots set date='%s',from_time='%s',to_time='%s' where time_slot_id='%s'"%(date,from_time,to_time,time_slot_id)
        update(yy)
      #   return """<script>alert('updated successfull');window.location='manage_timeslots';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">UPDATED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_timeslots';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
     if action=='delete':
        pu="delete from timeslots where time_slot_id='%s'"%(time_slot_id)
        delete(pu)
      #   return """<script>alert('deleted successfull');window.location='manage_timeslots';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">DELETED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_timeslots';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
     return render_template('admin/manage_timeslots.html',data=data)



@admin.route('/manage_trainer',methods=['get','post'])
def admin_manage_trainer():
   data={}
   q="select * from trainer"
   data['trainer']=select(q)
   if 'submit' in request.form:
        name=request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        register_number = request.form['register_np']
        district = request.form['district']
        image = request.files['image']
        path="static/images/"+str(uuid.uuid4())+image.filename
        image.save(path)
        username = request.form['username']
        password=request.form['username']
        m="insert into login values(NULL,'%s','%s','trainer')"%(username,password)
        m1=insert(m)
        q="insert into trainer values(NULL,'%s','%s','%s','%s','%s','%s','%s','pending')"%(m1,name,email,phone,register_number,district,path)
        insert(q)

   if 'action' in request.args:
        action=request.args['action']
        trainer_id=request.args['trainer_id']
   else:
        action=None
    
    
   if action=='update':
        fu="select * from trainer where trainer_id='%s'"%(trainer_id)
        data['updates']=select(fu)
   
   if 'update' in request.form:
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        register_number=request.form['register_np']
        district=request.form['district']

        yy="update trainer set name='%s',email='%s',phone='%s',register_number='%s',district='%s' where trainer_id='%s'"%(name,email,phone,register_number,district,trainer_id)
        update(yy)
      #   return """<script>alert('updated successfull');window.location='manage_trainer';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">UPDATED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_trainer';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
   if action=='delete':
       q="delete from trainer where trainer_id='%s'"%(trainer_id)
       delete(q)
      #  return """<script>alert('deleted successfull');window.location='manage_trainer';</script>"""
       return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">DELETED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_trainer';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
   return render_template('admin/manage_trainer.html',data=data)
      


@admin.route('/manage_equipments',methods=['get','post'])
def admin_manage_equp():
   data={}
   q="select * from equipments"
   data['equip']=select(q)
   if 'submit' in request.form:
      image=request.files['equp_image']
      equp_name=request.form['equp_name']
      path="static/"+str(uuid.uuid4())+image.filename
      image.save(path)
      m="insert into equipments values(NULL,'%s','%s' )"%(path,equp_name)
      insert(m)

   if 'action' in request.args:
        action=request.args['action']
        eqmt_id=request.args['eqmt_id']
   else:
        action=None
    
    
   if action=='update':
        fu="select * from equipments where eqmt_id='%s'"%(eqmt_id)
        data['updates']=select(fu)
   
   if 'update' in request.form:
        image=request.files['equp_image']
        equp_name=request.form['equp_name']
        path="static/"+str(uuid.uuid4())+image.filename
        image.save(path)
        yy="update equipments set equp_name='%s',image='%s' where eqmt_id='%s'"%(equp_name,path,eqmt_id)
        update(yy)
      #   return """<script>alert('updated successfull');window.location='manage_equipments';</script>"""
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">UPDATED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_equipments';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
   if action=='delete':
        pu="delete from equipments where eqmt_id='%s'"%(eqmt_id)
        delete(pu)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">DELETED</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'manage_equipments';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
   return render_template('admin/manage_equipments.html',data=data)



@admin.route('/view_user',methods=['get','post'])
def view_user():
   data={}
   q="select * from user"
   data['user']=select(q)
   return render_template('admin/view_user.html',data=data)


    

@admin.route('/logout', methods=['GET', 'POST'])
def logout():
            return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/img/gym1.gif" alt="Smiley Image" style="width: 200px; height: 150px;border-radius: 20px;">
        <h3 style="color: blue;">Logouted</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'login';
        }, 4000); // Redirect after 2 seconds
    </script>
"""


@admin.route('/view_feedback',methods=['get','post'])
def view_feedback1():
   data={}
   q="SELECT * FROM `feedback` INNER JOIN USER ON (user.user_id=feedback.user_id)"
   data['feed']=select(q)
   return render_template('admin/view_feedback.html',data=data)




# ------------------------------------------------------------andriod---------------------



@admin.route('/view_timeslots',methods=['post'])
def view_timeslots():
    data={}
    q="select * from timeslots"
    res=select(q)
    #  data['time']=res
    if len(res)>0:
        return jsonify(status ="ok",data=res)
    else:
        return jsonify(status="no")
    


@admin.route('/view_trainer',methods=['post'])
def view_trainer():
    data={}
    q="select * from trainer"
    res = select(q)
    if len(res)>0:
        return jsonify(status ="ok",data=res)
    else:
        return jsonify(status="no")


@admin.route('/view_category',methods=['post'])
def view_category():
    data={}
    q="select * from category"
    res = select(q)
    if len(res)>0:
        return jsonify(status = "ok",data=res)
    else:
        return jsonify(status="no")



@admin.route('/view_equipments',methods=['post'])
def view_equipments():
    data={}
    q="select * from equipments"
    res = select(q)
    if len(res)>0:
        return jsonify(status = "ok",data=res)
    else:
        return jsonify(status="no")