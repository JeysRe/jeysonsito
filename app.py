from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promociones - Restaurante Delicias</title>
    <style>
        /* Estilos CSS para dar formato */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .promotion {
            margin-bottom: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            overflow: hidden;
        }
        .promotion h2 {
            margin-top: 0;
            color: #666;
        }
        .promotion p {
            color: #777;
        }
        .promotion img {
            float: left;
            margin-right: 20px;
            border-radius: 8px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Promociones - Restaurante Delicias</h1>
    
    <div class="promotion">
        <img src="https://static.wixstatic.com/media/65a025_5cf78d2c1bf24f279a09769827e5668c~mv2.jpg/v1/fill/w_640,h_334,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/65a025_5cf78d2c1bf24f279a09769827e5668c~mv2.jpg" alt="Descuento de Apertura">
        <div>
            <h2>Descuento de Apertura</h2>
            <p>¡Visítanos en nuestra gran inauguración y obtén un 10% de descuento en tu primera compra!</p>
        </div>
    </div>
    
    <div class="promotion">
        <img src="https://www.menuspararestaurantes.com/wp-content/uploads/2022/12/promociones-en-tu-restaurante-combos2.jpg" alt="Happy Hour">
        <div>
            <h2>Happy Hour</h2>
            <p>De lunes a viernes de 5pm a 7pm, disfruta de nuestras bebidas alcohólicas con un 20% de descuento.</p>
        </div>
    </div>
    
    <div class="promotion">
        <img src="https://i0.wp.com/ofertasahora.com/wp-content/uploads/2018/10/Ultimos-dias-de-la-promocion-2x1-en-restaurante-la-pampa-OCtubre-2018.jpg?resize=794%2C1024&ssl=1" alt="Menú del Día">
        <div>
            <h2>Menú del Día</h2>
            <p>Cada día te ofrecemos un menú especial por solo $10. ¡No te lo pierdas!</p>
        </div>
    </div>
</div>

</body>
</html>

'''


if __name__ == "__main__":
    app.run(debug=True)
