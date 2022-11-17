from flask import Flask, render_template, url_for

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

@app.route("/a")
def a():
        return render_template("a.html")

@app.route("/b")
def b():
        return render_template("b.html")

@app.route("/c")
def c():
        return render_template("c.html")


@app.route("/d")
def d():
        return render_template("d.html")

@app.route("/e")
def e():
        return render_template("e.html")

@app.route("/search", methods=["POST"])
def move_forward():
    forward_message = "Moving Forward..."
    return render_template("search.html", forward_message=forward_message)


def win(matrix, m, o):
    k = 0
    for i in range(0, n):
        if(int(matrix[i][m]) == 1):
            k = k+1
    l = 0
    for i in range(0, n):
        if(int(matrix[o][i] == 1)):
            for j in range(0, n):
                if(matrix[j][i] == 1):
                    l = l+1
    return float(k/l)
  
  
def wout(matrix, m, o):
    k = 0
    for i in range(0, n):
        if(int(matrix[0][i]) == 1):
            k = k+1
    l = 0
    for i in range(0, n):
        if(int(matrix[o][i] == 1)):
            for j in range(0, n):
                if(matrix[i][j] == 1):
                    l = l+1
    return float(k/l)
  
  
def pagerank(matrix, o, n, p):
    a = 0
    for i in range(0, n):
        if(int(matrix[i][o]) == 1):
            k = 0
            for s in range(0, n):
                if(matrix[i][s] == 1):
                    k = k+1
            a = a+float((p[i]/k)*win(matrix, i, o)*wout(matrix, i, o))
    return a
  
  
n = 5
matrix = [[0,1,1,1,0],[1,0,0,1,0],[0,1,0,0,1],[1,0,1,0,1],[0,1,1,1,0]]
d = 0.85  # damping factor
  
o = 5
print("Number of iterations is:", o)
  
sum = 0
p = []
  
for i in range(0, n):
    p.append(1)
for k in range(0, o):
    for u in range(0, n):
        g = pagerank(matrix, u, n, p)
        p[u] = (1-d)+d*g
for i in range(0, n):
    sum += p[i]
    print("Page rank of node ", i+1, "is : ", p[i])
print("Sum of all page ranks: ", sum)
