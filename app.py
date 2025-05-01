from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(
    id=task_id_control,
    title=data['title'],
    description=data.get('description', '')
  )
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({
    "data": request.get_json()
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = []
  for task in tasks:
    task_list.append(task.to_dict())
  
  output = {
    "tasks": task_list,
    "total_tasks": len(tasks)
  }

  return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for task in tasks:
    if task.id == id:
     return jsonify(task.to_dict())
   
  return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break
  if task is None:
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

  data = request.get_json()
  task.title = data['title'] or task.title
  task.description = data['description'] or task.description
  task.completed = data['completed'] or task.completed
  return jsonify({"message": "Tarefa atualizada com sucesso"})



if __name__ == '__main__':
  app.run(debug=True)