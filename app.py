# FILE: app.py

#importacoin de programas de python
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import requests  # Import the requests module

#importacion de controladores
from controllers.auth_controller import AuthController

#ni idea ya ni me acuerdo para que sirve pero parece que es importante (ni me acerdo de donde lo saque) es lo de que siempre ocupe login
from utils import login_required

app = Flask(__name__)
app.secret_key = '2_baby_guinea_pigs'  


@app.route('/')
@login_required
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') == 'administrado':
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('admin_dashboard'))

## informacion grafica de la pagina
@app.route('/dashboard')
@login_required
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')
### informacion grafica de la pagina

### inicio de sesion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        if session.get('role') == 'administrador':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))
    controller = AuthController()
    return controller.login()

@app.route('/welcome')
@login_required
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html', username=session['username'])

@app.route('/inicio')
@login_required
def admin_dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') == 'administrador':
        return render_template('admin_dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/user_dashboard')
@login_required
def user_dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') != 'administrador':
        return render_template('admin_dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()  # Clear all session variables
    return redirect(url_for('login'))

    
# CRUD operations for nivel_educativo
@app.route('/nivel_educativo', methods=['GET'])
@login_required
def get_nivel_educativo():
    response = requests.get('http://localhost:3000/api/nivel_educativo')
    if response.status_code == 200:
        niveles = response.json()
        return render_template('nivel_educativo.html', niveles=niveles)
    else:
        return "Error al obtener los niveles educativos", response.status_code

@app.route('/nivel_educativo', methods=['POST'])
@login_required
def create_nivel_educativo():
    nivel = request.form.get('nivel')
    response = requests.post('http://localhost:3000/api/nivel_educativo', json={'nivel': nivel})
    if response.status_code == 201:
        return redirect(url_for('get_nivel_educativo'))
    else:
        return "Error al crear el nivel educativo", response.status_code

@app.route('/nivel_educativo/update/<int:id>', methods=['POST'])
@login_required
def update_nivel_educativo(id):
    nivel = request.form.get('nivel')
    response = requests.put(f'http://localhost:3000/api/nivel_educativo/{id}', json={'nivel': nivel})
    if response.status_code == 200:
        return redirect(url_for('get_nivel_educativo'))
    else:
        return "Error al actualizar el nivel educativo", response.status_code

@app.route('/nivel_educativo/delete/<int:id>', methods=['POST'])
@login_required
def delete_nivel_educativo(id):
    response = requests.delete(f'http://localhost:3000/api/nivel_educativo/{id}')
    if response.status_code == 204:
        return redirect(url_for('get_nivel_educativo'))
    else:
        return "Error al eliminar el nivel educativo", response.status_code
    

# CRUD operations for asuntos
@app.route('/asuntos', methods=['GET'])
@login_required
def get_asuntos():
    response = requests.get('http://localhost:3000/api/asuntos')
    if response.status_code == 200:
        asuntos = response.json()
        return render_template('asuntos.html', asuntos=asuntos)
    else:
        return "Error al obtener los asuntos", response.status_code

@app.route('/asuntos', methods=['POST'])
@login_required
def create_asunto():
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    response = requests.post('http://localhost:3000/api/asuntos', json={'titulo': titulo, 'descripcion': descripcion})
    if response.status_code == 201:
        return redirect(url_for('get_asuntos'))
    else:
        return "Error al crear el asunto", response.status_code

@app.route('/asuntos/update/<int:id>', methods=['POST'])
@login_required
def update_asunto(id):
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    response = requests.put(f'http://localhost:3000/api/asuntos/{id}', json={'titulo': titulo, 'descripcion': descripcion})
    if response.status_code == 200:
        return redirect(url_for('get_asuntos'))
    else:
        return "Error al actualizar el asunto", response.status_code

@app.route('/asuntos/delete/<int:id>', methods=['POST'])
@login_required
def delete_asunto(id):
    response = requests.delete(f'http://localhost:3000/api/asuntos/{id}')
    if response.status_code == 200:
        return redirect(url_for('get_asuntos'))
    else:
        return "Error al eliminar el asunto", response.status_code
    
    

# CRUD operations for alumnos
@app.route('/alumnos', methods=['GET'])
@login_required
def get_alumnos():
    response = requests.get('http://localhost:3000/api/alumnos')
    if response.status_code == 200:
        alumnos = response.json()
        return render_template('alumnos.html', alumnos=alumnos)
    else:
        return "Error al obtener los alumnos", response.status_code

@app.route('/alumnos', methods=['POST'])
@login_required
def create_alumno():
    nombre = request.form.get('nombre')
    apellido_paterno = request.form.get('apellido_paterno')
    apellido_materno = request.form.get('apellido_materno')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    response = requests.post('http://localhost:3000/api/alumnos', json={'nombre': nombre, 'apellido_paterno': apellido_paterno, 'apellido_materno': apellido_materno, 'telefono': telefono, 'correo': correo})
    if response.status_code == 201:
        return redirect(url_for('get_alumnos'))
    else:
        return "Error al crear el alumno", response.status_code

@app.route('/alumnos/update/<int:id>', methods=['POST'])
@login_required
def update_alumno(id):
    nombre = request.form.get('nombre')
    apellido_paterno = request.form.get('apellido_paterno')
    apellido_materno = request.form.get('apellido_materno')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    response = requests.put(f'http://localhost:3000/api/alumnos/{id}', json={'nombre': nombre, 'apellido_paterno': apellido_paterno, 'apellido_materno': apellido_materno, 'telefono': telefono, 'correo': correo})
    if response.status_code == 200:
        return redirect(url_for('get_alumnos'))
    else:
        return "Error al actualizar el alumno", response.status_code

@app.route('/alumnos/delete/<int:id>', methods=['POST'])
@login_required
def delete_alumno(id):
    response = requests.delete(f'http://localhost:3000/api/alumnos/{id}')
    if response.status_code == 204:
        return redirect(url_for('get_alumnos'))
    else:
        return "Error al eliminar el alumno", response.status_code
    


# CRUD operations for municipios
@app.route('/municipios', methods=['GET'])
@login_required
def get_municipios():
    response = requests.get('http://localhost:3000/api/municipios')
    if response.status_code == 200:
        municipios = response.json()
        return render_template('municipios.html', municipios=municipios)
    else:
        return "Error al obtener los municipios", response.status_code

@app.route('/municipios', methods=['POST'])
@login_required
def create_municipio():
    nombre_municipio = request.form.get('nombre_municipio')
    nombre_oficina = request.form.get('nombre_oficina')
    estado = request.form.get('estado')
    codigo_postal = request.form.get('codigo_postal')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    response = requests.post('http://localhost:3000/api/municipios', json={
        'nombre_municipio': nombre_municipio,
        'nombre_oficina': nombre_oficina,
        'estado': estado,
        'codigo_postal': codigo_postal,
        'telefono': telefono,
        'correo': correo
    })
    if response.status_code == 201:
        return redirect(url_for('get_municipios'))
    else:
        return "Error al crear el municipio", response.status_code

@app.route('/municipios/update/<int:id>', methods=['POST'])
@login_required
def update_municipio(id):
    nombre_municipio = request.form.get('nombre_municipio')
    nombre_oficina = request.form.get('nombre_oficina')
    estado = request.form.get('estado')
    codigo_postal = request.form.get('codigo_postal')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    response = requests.put(f'http://localhost:3000/api/municipios/{id}', json={
        'nombre_municipio': nombre_municipio,
        'nombre_oficina': nombre_oficina,
        'estado': estado,
        'codigo_postal': codigo_postal,
        'telefono': telefono,
        'correo': correo
    })
    if response.status_code == 200:
        return redirect(url_for('get_municipios'))
    else:
        return "Error al actualizar el municipio", response.status_code

@app.route('/municipios/delete/<int:id>', methods=['POST'])
@login_required
def delete_municipio(id):
    response = requests.delete(f'http://localhost:3000/api/municipios/{id}')
    if response.status_code == 204:
        return redirect(url_for('get_municipios'))
    else:
        return "Error al eliminar el municipio", response.status_code
    
    
    
# CRUD operations for turnos
@app.route('/turnos', methods=['GET'])
@login_required
def get_turnos():
    response = requests.get('http://localhost:3000/api/turnos')
    if response.status_code == 200:
        turnos = response.json()
        return render_template('turnos.html', turnos=turnos)
    else:
        return "Error al obtener los turnos", response.status_code

@app.route('/turnos', methods=['POST'])
@login_required
def create_turno():
    fecha_solicitud = request.form.get('fecha_solicitud')
    curp = request.form.get('curp')
    nombre_completo = request.form.get('nombre_completo')
    estado = request.form.get('estado')
    municipio_id = request.form.get('municipio_id')
    alumno_id = request.form.get('alumno_id')
    nivel_educativo_id = request.form.get('nivel_educativo_id')
    asunto_id = request.form.get('asunto_id')
    estatus_tramite = request.form.get('estatus_tramite')
    response = requests.post('http://localhost:3000/api/turnos', json={
        'fecha_solicitud': fecha_solicitud,
        'curp': curp,
        'nombre_completo': nombre_completo,
        'estado': estado,
        'municipio_id': municipio_id,
        'alumno_id': alumno_id,
        'nivel_educativo_id': nivel_educativo_id,
        'asunto_id': asunto_id,
        'estatus_tramite': estatus_tramite
    })
    if response.status_code == 201:
        return redirect(url_for('get_turnos'))
    else:
        return "Error al crear el turno", response.status_code

@app.route('/turnos/update/<int:id>', methods=['POST'])
@login_required
def update_turno(id):
    fecha_solicitud = request.form.get('fecha_solicitud')
    curp = request.form.get('curp')
    nombre_completo = request.form.get('nombre_completo')
    estado = request.form.get('estado')
    municipio_id = request.form.get('municipio_id')
    alumno_id = request.form.get('alumno_id')
    nivel_educativo_id = request.form.get('nivel_educativo_id')
    asunto_id = request.form.get('asunto_id')
    estatus_tramite = request.form.get('estatus_tramite')
    response = requests.put(f'http://localhost:3000/api/turnos/{id}', json={
        'fecha_solicitud': fecha_solicitud,
        'curp': curp,
        'nombre_completo': nombre_completo,
        'estado': estado,
        'municipio_id': municipio_id,
        'alumno_id': alumno_id,
        'nivel_educativo_id': nivel_educativo_id,
        'asunto_id': asunto_id,
        'estatus_tramite': estatus_tramite
    })
    if response.status_code == 200:
        return redirect(url_for('get_turnos'))
    else:
        return "Error al actualizar el turno", response.status_code

@app.route('/turnos/delete/<int:id>', methods=['POST'])
@login_required
def delete_turno(id):
    response = requests.delete(f'http://localhost:3000/api/turnos/{id}')
    if response.status_code == 204:
        return redirect(url_for('get_turnos'))
    else:
        return "Error al eliminar el turno", response.status_code
    









@app.route('/turnos/curp/<string:curp>', methods=['GET'])
@login_required
def get_turno_by_curp(curp):
    response = requests.get(f'http://localhost:3000/api/turnos/curp/{curp}')
    if response.status_code == 200:
        turno = response.json()
        return render_template('estatus_asunto.html', turno=turno)
    else:
        return "Error al obtener el turno", response.status_code



























































    
####    NO TOCAR    ####
# Nueva ruta para actualizar el estatus del turno basado en la CURP
@app.route('/turnos/actualizar', methods=['GET', 'POST'])
@login_required
def update_turno_estatus():
    if request.method == 'POST':
        curp = request.form.get('curp')
        estatus_tramite = request.form.get('estatus_tramite')
        response = requests.put(f'http://localhost:3000/api/turnos/estatus/{curp}', json={'estatus_tramite': estatus_tramite})
        if response.status_code == 200:
            return redirect(url_for('get_turnos'))
        else:
            return "Error al actualizar el estatus del turno", response.status_code
    return render_template('update_turno_estatus.html')

 
if __name__ == '__main__':
    
    app.run(debug=True)