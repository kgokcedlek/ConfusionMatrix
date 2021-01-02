#From Flask, I want to import Flask, render_template and request
from flask import Flask, render_template, request

#Declare the app
app = Flask(__name__)

# Start an app route which is '/'
@app.route('/')
#Declare the main function
def main():
    return render_template('app.html')

@app.route('/send',methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        num4 = request.form['num4']
        
        

        
        TP = float(num1)
        TN =float(num4)
        FP =float(num3)
        FN =float(num2)
        Accuracy= (TP + TN)/(TP+TN+FP+FN)
        Precision= (TP)/(TP+FP)
        Recall= (TP)/(TP+FN)
        F1Score= (2*Precision*Recall)/(Precision+Recall)
        AY=TP+FN
        AN=FP+TN
        PY=TP+FP
        PN=TN+FN

        return render_template('app.html', TP=TP,TN=TN,FP=FP,FN=FN,Accuracy=Accuracy,Precision=Precision,Recall=Recall,F1Score=F1Score,AY=AY,AN=AN,PY=PY,PN=PN)

        

        
        
        
        
        
        

if __name__ == '__main__':
    app.debug =True
    app.run()


