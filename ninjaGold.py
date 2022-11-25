from datetime import datetime
import random
from flask import Flask,render_template,session,request,redirect
app = Flask(__name__)
app.secret_key = "Keep it safe"
# ---------------------------------------------------------------
@app.route('/')
def index():
    session['totalGold'] = 0
    session['farmGold'] = 0
    session['caveGold'] = 0
    session['houseGold'] = 0
    session['casinoGold'] = 0
    session['activites'] = ''
    session['activitesCasino'] = ''
    session['sortActivite']=[]
    session['casinoCurrentGold']=[]
    return render_template("index.html")

@app.route('/procces_money',methods=['post'])
def procces_money():
    activeCurrentGold = None
    casinoCurrentGold = None
    if request.form['which_form'] =='farm':
        session['farmGold'] = random.randint(10,15)
        session['totalGold'] += int(session['farmGold'])
        activeCurrentGold ='Earned '+ str(int(session['farmGold'])) +' golds from the farm !  '+ str(datetime.now())
        
    elif request.form['which_form'] == 'cave':
        session['caveGold'] = random.randint(5,10)
        session['totalGold'] += int(session['caveGold'])
        activeCurrentGold ='Earned ' + str(int(session['caveGold'])) + ' golds from the cave !  ' + str(datetime.now())

    elif request.form['which_form'] == 'house':
        session['houseGold'] = random.randint(2,5)
        session['totalGold'] += int(session['houseGold'])
        activeCurrentGold ='Earned ' + str(int(session['houseGold'])) + ' golds from the house !  ' + str(datetime.now()) 
       
    elif request.form['which_form'] == 'casino':
        session['casinoGold'] = random.randint(-50,50)
        session['totalGold'] += int(session['casinoGold'])
        casinoCurrentGold = 'Earned ' + str(int(session['casinoGold'])) + ' golds from the casino !  ' + str(datetime.now())
    
    if casinoCurrentGold!=None:     
        session['casinoCurrentGold'].insert(0,casinoCurrentGold)
    if activeCurrentGold!=None:
        session['sortActivite'].insert(0,activeCurrentGold)
    return redirect('/goGold')

@app.route('/goGold')
def goGold():
    return render_template("index.html")

@app.route('/reset')
def reset():
    return redirect('/')
# ---------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)