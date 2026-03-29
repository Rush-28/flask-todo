from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []
next_id = 1

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    task = request.form.get("task", "").strip()
    if task:
        todos.append({"id": next_id, "task": task})
        next_id += 1
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)