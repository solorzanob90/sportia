<?php require_once "./conectaBD.php"; ?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div><a href="index.php"><img src="./imagenes/inicio.png" alt="" width="32" height="32"> </a> </div>
</body>
</html>

<?php

//Datos del cliente
$ident=$_POST['ident'];
$nomCl=$_POST['nomCl'];
$apeCl=$_POST['apeCl'];
$tel=$_POST['tel'];
$dir=$_POST['dir'];
$eml=$_POST['eml'];
/************************/

//Datos de la venta
$id=$_POST['id'];
$precio=$_POST['precio'];
$cantidad=$_POST['cant'];
$total=$_POST['total'];
$stock=$_POST['stock'];
/**************************/


$existClient = mysqli_query($conn, "select cedula from cliente where cedula=$ident");
$result = mysqli_num_rows($existClient);
$numPedido = rand(1,999999);

if($result>0) //Hay clientes registrados
{
    //me guardas una venta
    mysqli_query($conn, "INSERT INTO `ventas`(`id_pedido`, `cedula`, `total`, `estado`) 
    VALUES ($numPedido,$ident,$total,'pagado')");

    //me guardas el detalle de la venta
    mysqli_query($conn, "INSERT INTO `detalleventas`(`id_pedido`, `id_producto`, `cantidad`) VALUES ($numPedido,$id,$cantidad)");

    //reduces el stock del producto seleccionado
    mysqli_query($conn,"UPDATE `productos` SET `stock`=$stock-$cantidad WHERE id_producto=$id");

       ?>
         <img src="./imagenes/verificado.gif" alt="">
      <?php

    echo "venta realizada"."\n";
        
}else{

    //guardame el cliente
    mysqli_query($conn, "INSERT INTO `cliente`(`cedula`, `nombre`, `apellido`, `telefono`, `direccion`, `email`)
    VALUES ($ident,'$nomCl','$apeCl',$tel,'$dir','$eml')");

    //me guardas una venta
    mysqli_query($conn, "INSERT INTO `ventas`(`id_pedido`, `cedula`, `total`, `estado`) 
    VALUES ($numPedido,$ident,$total,'pagado')");

    //me guardas el detalle de la venta
    mysqli_query($conn, "INSERT INTO `detalleventas`(`id_pedido`, `id_producto`, `cantidad`) VALUES ($numPedido,$id,$cantidad)");

    //reduces el stock del producto seleccionado
    mysqli_query($conn,"UPDATE `productos` SET `stock`=$stock-$cantidad WHERE id_producto=$id");
  
       ?>
         <img src="./imagenes/verificado.gif" alt="">
      <?php
   echo "venta realizada". "\n";
}

?>


