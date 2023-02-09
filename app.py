#app.py
from flask import Flask, request, render_template, jsonify, json
from query.queries import totalrecords, totalrecordwithfilters, alldata

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route("/ajaxfile",methods=["POST","GET"])
def ajaxfile():
    try:
        if request.method == 'POST':
            
            draw = request.form['draw'] 
            row = int(request.form['start'])
            rowperpage = int(request.form['length'])
            searchValue = request.form["search[value]"]
            likeString = "%" + searchValue +"%"
            totalRecords=totalrecords()
            # print(totalRecords) 
            ## Total number of records with filtering
            totalRecordwithFilter =  totalrecordwithfilters(likeString)
            # print(totalRecordwithFilter) 
 
            ## Fetch records
            data=alldata(searchValue,likeString, row, rowperpage)
 
            response = {
                'draw': draw,
                'iTotalRecords': totalRecords,
                'iTotalDisplayRecords': totalRecordwithFilter,
                'aaData': data,
            }
            return jsonify(response)
    except Exception as e:
        print(e)
    
 
if __name__ == "__main__":
    app.run(debug=True)