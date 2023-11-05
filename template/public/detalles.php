<?php require_once "./conectaBD.php"; ?>

<?php 
$id= $_POST['id'];
$nombre= $_POST['nombre'];
$precio= $_POST['precio'];
$stock= $_POST['stock'];
$cantidad= $_POST['cantidad'];
$total=$cantidad*$precio;
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/detalle.css">
    <title>Detalles de Compra</title>
</head>
<body>
    <header id="encabDetal">
    <h3>SPORTIA</h3>
    <H4>Tu tienda de articulos deportivos</H4>
    </header>
    <nav id="nav">
      <a href="index.php"><img src="./imagenes/inicio.png" alt="" width="32" height="32"> </a> 
    </nav>
    
    <form action="confirmarPedido.php" method="post" id="frm">

    <fieldset>
        <legend>Ingresar datos del cliente</legend>
     <div id="datClient">
     <p class="dcli"><label for="">NOMBRE DEL CLIENTE: </label><input type="text" required pattern="[A-Za-z]{1,50}" id="nomCliente" name="nomCl"></p>
     <p class="dcli"><label for="">APELLIDO DEL CLIENTE: </label><input type="text" required pattern="[A-Za-z]{1,50}" id="apeCliente" name="apeCl"></p>
     <p class="dcli"><label for="">IDENTIFICACIÓN: </label><input type="number" min="0" max="9999999999" required pattern="[0-9]{0-10}" title="escriba 10 digitos" id="identificación" name="ident"></p>
     <p class="dcli"><label for="">TELEFONO: </label><input type="tel" max="10" min="0" max="9999999999" required pattern="[0-9]{0-10}"  class="cjTx" id="teléfono" name="tel"></p>
     <p class="dcli"><label for="">DIRECCIÓN: </label><input type="text" required  id="dir" name="dir"></p>
     <p class="dcli"><label for="">CORREO ELECTRÓNICO: </label><input type="email" required pattern="[^@\s]+@[^@\s]+\.[^@\s]+" id="email" name="eml"></p>
      <!--<div><label for="">TARJETA DE CREDITO: </label><input type="number"  id="TC">CVC<input type="number" class="cjTx" id=cvc"></div>-->
     </div>
     </fieldset>
    
     <input type="number" value="<?php echo $id ?>" name="id" hidden>
     <input type="number" value="<?php echo $precio ?>" name="precio" hidden>
     <input type="number" value="<?php echo $total ?>" name="total" hidden>
     <input type="number" value="<?php echo $cantidad ?>" name="cant" hidden>
     <input type="number" value="<?php echo $stock ?>" name="stock" hidden>

     <div id="detallesCompra">
        <p>NOMBRE DEL PRODUCTO: <?php echo $nombre; ?></p>
        <p>CANTIDAD :<?php echo $cantidad; ?> UNIDADES</p>
        <p>TOTAL DE LA COMPRA: <?php echo $total; ?></p>
    </div>

    </form>
    <input id="submit" type="submit" value="Confirmar" name="enviar" form="frm">

   

     

</body>
</html>





