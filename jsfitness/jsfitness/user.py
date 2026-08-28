from flask import *
from database import *


user=Blueprint('user',__name__)



@user.route('/user_feedback',methods=['post'])
def user_feedback():
    user_id=request.form['uid']
    feedback = request.form['feedback']
    m="insert into feedback values(NULL,'%s','%s')"%(user_id,feedback)
    insert(m)
    return jsonify(status = "ok")
    # data={}
    # q="select * from equipments"
    # res = select(q)
    # if len(res)>0:
    #     return jsonify(status = "ok",data=res)
    # else:
    #     return jsonify(status="no")



@user.route('/user_booking',methods=['post'])
def user_booking():
    user_id=request.form['uid']
    time_slot_id=request.form['time_id']
    trainer_id=request.form['t_id']
    catgory_id = request.form['cat_id']
    eqmt_id=request.form['eqpt_id']
    amount = 600
    m="insert into booking Values(NULL,'%s','%s','%s','%s','%s','%s')"%(user_id,time_slot_id,trainer_id,catgory_id,eqmt_id,amount)
    insert(m)
    return jsonify(status ='ok')


@user.route('/view_workouts',methods=['post'])
def view_workouts():
    data={}
    # q="SELECT * FROM `circuits` INNER JOIN `circuit_sub` ON(circuits.`c_id`=circuit_sub.`c_id`)"
    q="SELECT * FROM `workouts`"
    data['view'] = select(q)
    res = select(q)
    # if len(res)>0:
    return jsonify(status = "ok",data=res)
    # else:
    #     return jsonify(status="no")
   

@user.route('/view_payment_details',methods=['post'])
def view_payment_details():
    data={}
    q="select * from `booking`"
    data['view']=select(q)
    res = select(q)
    return jsonify(status="ok",data=res)


  


