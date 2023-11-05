<?php require_once "./conectaBD.php"; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/compra.css">
    <title>SPORTIA</title>
</head>
<body>
    <header id="encab">
    <h3>SPORTIA</h3>
    <H4>Tu tienda de articulos deportivos</H4>
    </header>
    <nav id="nav">
      <a href="index.php"><img src="./imagenes/inicio.png" alt="" width="32" height="32"> </a> 
    </nav>
    <?php
    $id=$_POST['id'];
   //f $id= (int) $id;
    $query = mysqli_query($conn, "select * from productos where id_producto=$id");
    $result = mysqli_num_rows($query);
    if($result>0)
    {
 while ($data = mysqli_fetch_assoc($query)) { ?>

      <div id=tarjCompra>
          <div id="ima">
              <img  src="./imagenes/<?php echo $data['imagen']; ?>" alt="..." id="imga" width="400px" height="400px"/>
          </div>
             <div id="detalles">
                <!--Se muestran los datos del producto-->
                <form action="detalles.php" method="post">
                <p style="font-size: 50px;" id="nom"><?php echo $data['nombre']; ?></p>
                <p id="desc"><?php echo $data['descripcion']; ?></p>
                <P id="prec"><?php echo '$'.$data['precio']; ?></P>

               <!--Se toman los datos-->
                <input type="text" name="id" value="<?php echo $data['id_producto']; ?>" hidden>
                <input type="text" name="nombre" value="<?php echo $data['nombre']; ?>" hidden>
                <input type="text" name="precio" value="<?php echo $data['precio']; ?>" hidden>
                <input type="text" name="stock" value="<?php echo $data['stock']; ?>" hidden>


               <?php 
                if($data['stock']>0){?>
                 <label for="">Cantidad <input type="number" value="1" min=1 size=5 name="cantidad" max="<?php echo $data['stock']; ?>"/> de <?php echo $data['stock']; ?> disponibles</label>

                <?php }else echo "Agotado"
                
                ?> <br><br>
                <input type="submit" id=comprar value="comprar">
                </form>
             </div>

      </div>



   <?php }

    }?>
    
    
     <div id="tarjCompra">
       
     </div>
</body>
</html>