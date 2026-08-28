import uuid
from flask import *
from database import *


trainer=Blueprint('trainer',__name__)


@trainer.route('/trainer_home',methods=['get','post'])
def trainer_home():
    return render_template('trainer/trainer_home.html')





@trainer.route('/workout',methods=['get','post'])
def trainer_workout():
    data={}
    q="select * from workouts"
    data['work']=select(q)
    if 'submit' in request.form:
        name = request.form['name']
        description=request.form['description']
        image = request.files['image']
        path="C:/Users/hp/Documents/jsfitness/jsfitness/jsfitness/static/images/"+str(uuid.uuid4())+image.filename
        image.save(path)
        m="insert into workouts values(NULL,'%s','%s','%s')"%(path,name,description)
        insert(m)
    

    if 'action' in request.args:
        action=request.args['action']
        workout_id=request.args['workout_id']
    else:
        action=None
    if action=='delete':
        pu="delete from workouts where workout_id='%s'"%(workout_id)
        delete(pu)
    return render_template('trainer/workout.html',data=data)
  

@trainer.route('/manage_circuits',methods=['get','post'])
def manage_circuits():
    if 'submit' in request.form:
        c_name = request.form['c_name']
        purpose=request.form['purpose']
        m="insert into circuits values(NULL,'%s','%s')"%(c_name,purpose)
        insert(m)
    return render_template('trainer/manage_circuits.html')


@trainer.route('/manage_circuitsub',methods=['get','post'])
def manage_circuitsub():
    data={}
    # q="SELECT * FROM `circuits` INNER JOIN `circuit_sub` ON(circuits.`c_id`=circuit_sub.`c_id`)"
    # data['view'] = select(q)
    m="select * from circuits"
    data['circuits']=select(m)
    # -----------------------------------
    n="select * from workouts"
    data['workouts']=select(n)
    if 'submit' in request.form:
        c_id=request.form['circuits']
        workout_id=request.form['workouts']
        times = request.form['times']
        m="insert into circuit_sub values(NULL,'%s','%s','%s')"%(c_id,workout_id,times)
        insert(m)
    return render_template('trainer/manage_circuitsub.html',data=data)


