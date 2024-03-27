from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarjeta de Presentación</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"> <!-- Agrega Font Awesome -->
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 20px;
        }
        .card {
            background-color: #FAE5D3; /* Cambia el color de fondo según tu preferencia */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 40px; /* Ajusta este valor para aumentar los márgenes */
            max-width: 300px;
            margin: auto;
            text-align: center;
        }
        .card img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin-bottom: 20px;
        }
        .card h1 {
            margin-bottom: 10px;
            font-size: 24px;
            color: #333333; /* Cambia el color del texto según tu preferencia */
        }
        .card p {
            margin-bottom: 20px;
            font-size: 18px;
            color: #666666; /* Cambia el color del texto según tu preferencia */
        }
        .social-icons a {
            margin-right: 10px;
            color: #666666;
            text-decoration: none;
        }
    </style>
</head>
<body>

<div class="card">
    <img src="https://images.pexels.com/photos/2272853/pexels-photo-2272853.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt="Profile Picture">
    <h1>Sarah Estephany Nuñez</h1>
    <p>Desarrolladora Web</p>
    <p>Correo Electrónico: sharon@gmail.com</p>
    <p>Teléfono: +51 915942185</p>
    <div class="social-icons">
        <a href="https://facebook.com"><i class="fab fa-facebook-f"></i></a>
        <a href="https://wa.me/51915942185"><i class="fab fa-whatsapp"></i></a>
        <a href="https://instagram.com"><i class="fab fa-instagram"></i></a>
    </div>
</div>

</body>
</html>
'''


if __name__ == "__main__":
    app.run(debug=True)
