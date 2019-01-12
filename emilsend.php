<?php

//echo $_REQUEST['emailid'];
  if (isset($_REQUEST['emailid'])) 
                    {
                    $emailid = $_REQUEST['emailid'];
                    //echo $imageid;
                    $hostname = 'devta.c6obkwbtq8na.us-east-2.rds.amazonaws.com'; //localhost
                    $username = 'akhilgupta';
                    $password = '8171834923';
                    $database = 'irrs'; //androiduploadimage
                 
                    $conn = mysqli_connect($hostname,$username,$password,$database)
                    or die("Unable to connect with the Server."); 
                   //$b = system('test.py',$a);
                     // echo shell_exec("python testing4.py $imageid");
                      //echo $b;
                require 'PHPMailerAutoload.php';
                //require 'credentials.php';


                $mail = new PHPMailer;


                $mail->SMTPDebug = 2;                               // Enable verbose debug output

                $mail->isSMTP();                                      // Set mailer to use SMTP
                $mail->Host = 'smtp.gmail.com';  // Specify main and backup SMTP servers
                $mail->SMTPAuth = true;                               // Enable SMTP authentication
                $mail->Username = 'akhil.1613009@kiet.edu';                 // SMTP username
                $mail->Password = ''; //pass                           // SMTP password
                $mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
                $mail->Port = 587;                                    // TCP port to connect to

                $mail->setFrom('akhil.1613009@kiet.edu','akhil');
                $mail->addAddress($emailid);     // Add a recipient
                //$mail->addAddress('ellen@example.com');               // Name is optional
                $mail->addReplyTo('akhil.1613009@kiet.edu');

                //$mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
                //$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
                $mail->isHTML(true);                                  // Set email format to HTML

                $mail->Subject = 'Information regarding the provided image';
                $mail->Body    = 'Your query is in <b>processing.</b>';
                $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

                if(!$mail->send()) {
                    echo 'Message could not be sent.';
                    echo 'Mailer Error: ' . $mail->ErrorInfo;
                } else {
                     echo '<script type="text/javascript">  window.onload = function(){
      alert("Mail has been send to the registered account");
    }</script>';
                     } 

                }
            
            else echo "mail not send";
?>