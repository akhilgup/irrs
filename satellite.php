<!DOCTYPE html>
<html lang="en">

      <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Akhil is PRO</title>
      <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/semantic.min.css">
      <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:400,600,700" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Comfortaa:400,700" rel="stylesheet">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">
      <link rel="stylesheet" href="css/style.css">
      </head>

    <body>
     <nav>
       <ul class="brand-logo">
          <a href="#">
            <img src="http://4.bp.blogspot.com/_J3v765bIS9A/S18Q5W7xupI/AAAAAAAAA2Y/-tnW72pqw0k/s640/indian_map.gif" alt="logo">
          </a>
       </ul>
          <ul class="nav-links">
                <li><a href="index.html">Complaints</a></li>
                <li><a href="http://localhost:8080/satellite.php">Satellite images</a></li>
                <li><a href="#">Satellite analysis</a></li>
                <li><a href="#">Real time monitoring</a></li>
          </ul>
      </nav>
          <br>
            <div class="container">
              <div class="fluid-container">
                <div class="c-label">Uttar pradesh
                </div>
                  <br>
                  <br>
                     <div class="ui segment">
                       <div class="row col-lg-12">
                          <div class="col-lg-2">
                             <!-- image fetch from database-->
                              <?php
                                 $conn = mysqli_connect('127.0.0.1','root','akhilgupta','hack');
                                 $sql = "SELECT * FROM image_input";
                                 $result = mysqli_query($conn,$sql);
                                 while ($row = mysqli_fetch_array($result)){
                                   
                                       $image_name = $row["image_name"];
                                       $image_path = $row["image_path"];
                                       echo "<img height = '128' width = '138' src = 'images/$image_name'>";
                                       echo '<br>';
                                       $imageid = $row["id"];
                                       ?>

                                      <!-- html button as a link -->
                                       <a href ="satelliteanalysis.php?imageid=<?php echo $imageid ?>">
                                       <button class="col-lg-12 btn btn-info" style="margin-top:4px;" name="submit" value="submit">check</button></a>
                                       <br>
                                       <br>
                                      
                                     </div>
                                    <div class="col-lg-2">
                                    <?php
                                    }
                                    ?>
                                    </div>
                                    
                        </div>
                    </div>
                 </div>
             </div>

      </body>
</html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
