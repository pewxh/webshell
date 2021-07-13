from flask import  Flask,render_template,request
import subprocess 

app = Flask(__name__)

@app.route("/")
def root():
  return render_template('index.html')

@app.route('/run',methods=['GET'])
def run():
    cmd = request.args.get('cmd')
    output = subprocess.getoutput(cmd)
    return render_template('cmd.html',data=[output])
    


app.run(debug=False,host='0.0.0.0')