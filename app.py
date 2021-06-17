from flask import Flask, request, render_template
from dao import EmpDAO
from dto import EmpDTO

# from dto import EmpDTO

app = Flask(__name__)

@app.route('/', methods=['get'])
def get():
    return render_template('reqres.html')  #http://127.0.0.1:5000/reqres.html url 의미


@app.route('/getdata', methods=['get'])
def getdata():
    return '{"name":"재석", "age":49}'



@app.route("/getemp", methods=['post'])
def datemp():
    data = EmpDAO().empone(request.form.get('empno') ) # select 후에 json 포멧의 문자열로 가공해서 반환하는 메소드 호출 
    return data

@app.route("/insert", methods=['post'])
def insertemp():
    dto = EmpDTO(request.form.get('empno'), request.form.get('ename'), request.form.get('sal'))
    EmpDAO().empinsert(dto)
    return EmpDAO().empone(request.form.get('empno'))

@app.route("/update", methods=['post'])
def updateemp():
    select = EmpDAO().empone(request.form.get('empno'))
    if select:
        dto = EmpDTO(request.form.get('empno'), request.form.get('ename'), request.form.get('sal')) # EmpDTO 클래스 생성 및 맴버변수 할당
        EmpDAO().empupdate(dto)
        return EmpDAO().empone(request.form.get('empno'))
    else:
        return ''

@app.route("/delete", methods=['post'])
def deleteemp():
    select = EmpDAO().empone(request.form.get('empno'))
    if select:
        print(request.form.get('empno'))
        EmpDAO().empdelete(request.form.get('empno'))
        return '삭제완료'
    else:
        return ''


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")