<?php
/**
* Created by PhpStorm.
* User: Vlad
* Date: 2/22/2018
* Time: 4:47 PM
*/
//Header
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
require_once dirname(__FILE__) . '/FileHandler.php';
 $upload = new FileHandler();
 $account_details = array();
//Make sure that it is a POST request.
if (strcasecmp($_SERVER['REQUEST_METHOD'], 'POST') != 0) {
   throw new Exception('Request method must be POST!');
}
$description = null;

//added after updation
//added after updation
//added after updation


$com_name = null;
$email = null;
// $lat = null;
// $lon = null;

if (isset($_POST["desc"]) && isset($_POST["com_name"]) && isset($_POST["email"])) {
   $description = $_POST["desc"];
   $com_name = $_POST["com_name"];
   $email = $_POST["email"];
   echo ini_get('post_max_size');
   echo ini_get('upload_max_filesize');
   // $lat = $_POST["lat"];
   // $lon = $_POST["lon"];
}

// if (isset($_POST["desc"])) {
//    $description = $_POST["desc"];
// }
$profilepic = $_FILES["image"];
// if ($profileUpdateStatus = $upload->updateprofilepic($description,$profilepic)) {
//    if ($profileUpdateStatus == "success") {
//        // $account_details['info'] = $database->echoMessage("success", "Image successfully updated");
//     $account_details['info'] ="success";$account_details['message'] =  "Image successfully updated";
//        echo json_encode($account_details);
//        // $account->updateimageurl(dirname(__FILE__));
//        // $account->updatenumberpicupdated();
//        // $post->uid = $account->uid;
//        // $postcount = count($post->getuserpid());
//        // $account->setuppopularity($postcount);
//    } else {
//        $account_details['info'] ="error";$account_details['message'] =  "Image not updated";
//        echo json_encode($account_details);
//    }
// } else {
//    // $account_details['info','message'] = ("error", "Error uploading image");
//    $account_details['info'] ="error";$account_details['message'] =  "Error uploading image";
//    echo json_encode($account_details);
// }


if ($profileUpdateStatus = $upload->updateprofilepic($description,$profilepic,$com_name,$email)) {
   if ($profileUpdateStatus == "success") {
       // $account_details['info'] = $database->echoMessage("success", "Image successfully updated");
    $account_details['info'] ="success";$account_details['message'] =  "Image successfully updated";
       echo json_encode($account_details);
       // $account->updateimageurl(dirname(__FILE__));
       // $account->updatenumberpicupdated();
       // $post->uid = $account->uid;
       // $postcount = count($post->getuserpid());
       // $account->setuppopularity($postcount);
   } else {
       $account_details['info'] ="error";$account_details['message'] =  "Image not updated";
       echo json_encode($account_details);
   }
} else {
   // $account_details['info','message'] = ("error", "Error uploading image");
   $account_details['info'] ="error";$account_details['message'] =  "Error uploading image";
   echo json_encode($account_details);
}

// mysqli_close($db);
return;