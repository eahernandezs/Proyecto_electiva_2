from flask import Flask,render_template,request
import boto3
app = Flask(__name__,static_url_path='',static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solicitud", methods=["POST"])
def solicitar():
    hora1 = request.form.get("hora1")
    hora2 = request.form.get("hora2")
    hora3 = request.form.get("hora3")
    
    datos_a_enviar = "{},{},{}\n".format(float(hora1),float(hora2),float(hora3))
    
    end_point = "sagemaker-scikit-learn-2022-12-02-22-51-57-664"
    

    client = boto3.client("sagemaker-runtime","us-east-1")


    response = client.invoke_endpoint(EndpointName=end_point,Body=2*datos_a_enviar,ContentType="text/csv")
    prediction = response['Body'].read()
    print(prediction)
    return f"{prediction}"



if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)



