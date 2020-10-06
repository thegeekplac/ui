from flask import Flask, render_template, url_for, redirect, request




app = Flask(__name__)

num=5
val={}
def get_values(num):
    list_of_val=[]
    for i in range(num*3):
        list_of_val.append("select%s"%(i))
    return (list_of_val)
def val_eraser(dict):
    for i in range(len(dict)):
        if dict[list(dict.keys())[i]][:2]!="val":
            dict[list(dict.keys())[i]]=" "
    return dict
list2 =[]
list1=[]
email=""
@app.route("/", methods=['GET', 'POST'])
def index():
    global num
    global val
    global list2
    global list1
    global email
    list2 = get_values(num)
    list1 = list2.copy()
    for i in range(len(list2)):
        list2[i] = request.form.get(list2[i])

    if request.method == 'POST':
        if request.form.get('add') == 'add':
            num=num+1
            val = val_eraser({list1[i]: list2[i] for i in range(len(list2))})

        elif request.form.get('remove') == 'remove':
            num=num-1
            val = val_eraser({list1[i]: list2[i] for i in range(len(list2))})
        elif request.form.get('reset') == 'reset':
            val = ({list1[i]: " " for i in range(len(list2))})
            return render_template("index.html", num=num, values=val)
        elif request.form.get('send') == 'send':
            if len(val)==0:
                val={list1[i]: list2[i] for i in range(len(list2))}
            email=request.form.get("email")
        else:
            return render_template("index.html",num=num,values=val)

        val = {list1[i]: list2[i] for i in range(len(list2))}
    for i in range(len(list2)):
        list2[i] = request.form.get(list2[i])
    return render_template("index.html",num=num,values=val)




if __name__ == '__main__':
    app.run(debug=True)
