
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
      <li><a href="index.php">Complaints</a></li>
      <li><a href="satellite.php">Satellite images</a></li>
      <li><a href="#">Satellite analysis</a></li>
      <li><a href="#">Real time monitoring</a></li>
    </ul>
  </nav>

  <div class="container">
    <div class="fluid-container">
      <div class="c-label">Complains</div>


           
                <?php
                                 $conn = mysqli_connect('devta.c6obkwbtq8na.us-east-2.rds.amazonaws.com',     'akhilgupta','8171834923','irrs');
                                 $sql = "SELECT * FROM images";
                                 $result = mysqli_query($conn,$sql);
                                 while ($row = mysqli_fetch_array($result)){
                                      
                                      ?>

                                      <div class="ui segment">
                                      <div class="row col-lg-12">
                                      <div class="col-lg-2">
                                        <?php
                                       $url = $row["url"];
                                       $description = $row["description"];
                                       $complaint_heading = $row["complaintname"];
                                       $emailid = $row["emailid"];
                                       $location = $row["location"];

                                       echo "<img height = '128' width = '138' src = $url>";
                                       echo '<br>';
                                       $imageid = $row["id"];
                                       
                                       // <img class="ui small image" src="test.jpg">
                                       ?>
                                                  <a href="emilsend.php?emailid=<?php echo $emailid ?>">
                                                  <button class="col-lg-12 btn btn-success" style="margin-top:4px;" name="submit" value="submit">Test</button>
                                                  </a>
                                                  <?php
                                                 echo "<button class='col-lg-12 btn btn-info' style='margin-top:4px;' onclick='myfunction();';>Assign</button>";
                                                 ?>
                                                         <br>
                                                         <br>
                                                    </div>
                     
                                               
                                                  <div class="col-lg-10">
                                                    <?php
                                                  echo "<h3 class='c-complain-title'> $complaint_heading </h3>
                                                  <hr>";?>
                                                  <p class="c-complain-text">
                                                    <?php
                                                  echo "<p style='float:left; font-size:16px;''><i class='fas fa-map-marker-alt'></i>$location</p>";
                                                  echo "<br><br>
                                                                    <p> $description </p>";
                                                  echo "<p style='float:right; font-size:16px;'><i class='fas fa-user'></i>  $emailid </p>";
                                                  ?>

                                                            </div>
                                                        </div>
                                                      </div>
                                                     
                                                                   
                                    <?php
                                
                                    }
                                  
                                    ?>
                                  </div>
            </body>

</html>
<script>
      function myfunction() {
    alert("Workers has been assigned");
}
    </script>
