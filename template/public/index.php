<?php require_once "./conectaBD.php"; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/index.css">
    <title>Sport</title>
</head>
<body>
    <header id="encabezado">
    <h3>SPORTIA</h3>
    <H4>Tu tienda de articulos deportivos</H4>
    </header>
    <nav id="nav">
      <a href="index.php"><img src="./imagenes/inicio.png" alt="" width="32" height="32"> </a> 
    </nav>
    
    <section id="secc">
        
                <?php
                $query = mysqli_query($conn, "select * from productos");
                $result = mysqli_num_rows($query);
                if ($result > 0) {
                    while ($data = mysqli_fetch_assoc($query)) { ?>
                        
                            <div id="tarjeta" class="card">
                                <!-- Sale badge-->
                                <form action="comprar.php" method="post">
                                <!-- Product image-->
                                <?php
                                 if($data['stock']>0){?>
                                <input type="image" id="imga" src="./imagenes/<?php echo $data['imagen']; ?>" alt="Submit" height="300px" width="300px"/>
                
                                <?php } 
    
                                else { ?>
                                <input type="image" disabled id="imga" src="./imagenes/<?php echo $data['imagen']; ?>" alt="" height="300px" width="300px"/>
                                <p id="agotado">AGOTADO</p>
                                <?php } ?>  
                                <!-- Product price-->
                                <div  id="precio">PRECIO:<?php echo ($data['precio'] ); ?></div>
                                  <!-- Product name-->
                                 <h5 id="nombre">NOMBRE:<?php echo $data['nombre'] ?></h5>
                                        <!-- Product name-->
                                 <p id="marca">MARCA:<?php echo $data['marca']; ?></p>
                                        
                                <!-- Product actions-->
                    
                                
                                 <input type="number" hidden value="<?php echo $data['id_producto']; ?>" name="id" >   
                                 
                                </form>
                            </div>
                        
                <?php  }
                } ?>

            
       
    </section>
     
    
</body>
</html>