<?php
/**
 * Created by PhpStorm.
 * User: Belal
 * Date: 10/5/2017
 * Time: 11:53 AM
 */
 
require_once dirname(__FILE__) . '/FileHandler.php';
 
$response = array();
 
if (isset($_GET['apicall'])) {
    switch ($_GET['apicall']) {
        case 'upload':
 
            if (isset($_POST['desc']) && strlen($_POST['desc']) > 0 && $_FILES['image']['error'] === UPLOAD_ERR_OK) {
                $upload = new FileHandler();
                
                $file = $_FILES['image']['tmp_name'];
                
                //complaint krne waale ka naam
                $com_name = $_POST['com_name'];
                $email = $_POST['email'];
                //$lat = $_POST['lat'];
                //$lon = $_POST['lon'];

                $desc = $_POST['desc'];
 
                // if ($upload->saveFile($file, getFileExtension($_FILES['image']['name']), $desc)) {
                //     $response['error'] = false;
                //     $response['message'] = 'File Uploaded Successfullly';
                // }
                if ($upload->saveFile($file, getFileExtension($_FILES['image']['name']), $desc, $com_name, $email)) {
                    $response['error'] = false;
                    $response['message'] = 'File Uploaded Successfullly';
                }
 
            } else {
                $response['error'] = true;
                $response['message'] = 'Required parameters are not available';
            }
 
            break;
 
        case 'getallimages':
 
            $upload = new FileHandler();
            $response['error'] = false;
            $response['images'] = $upload->getAllFiles();
 
            break;
    }
}
 
echo json_encode($response);
 
function getFileExtension($file)
{
    $path_parts = pathinfo($file);
    return $path_parts['extension'];
}

