<?php
 
/**
 * Created by PhpStorm.
 * User: Belal
 * Date: 10/5/2017
 * Time: 11:30 AM
 */
class FileHandler
{
 
    private $con;
 
    public function __construct()
    {
        require_once dirname(__FILE__) . '/DbConnect.php';
 
        $db = new DbConnect();
        $this->con = $db->connect();
    }
    

    //$uid main description hain
   //  public function updateprofilepic($uid,$profilepic) {
   //     $temp_array = array();
   //     if (is_uploaded_file($profilepic["tmp_name"])) {
   //         $tmp_file = $profilepic["tmp_name"];
   //         $image_name = $uid."_".time().'.png';
   //         // $upload_dir = './image/'.$image_name.'.png';
   //         $filedest = dirname(__FILE__) . UPLOAD_PATH . $image_name;
   //         if (move_uploaded_file($tmp_file,$filedest)) 
   //         {
   //              $name = "http://192.168.43.40:8081/ImageUploadApi/uploads/".$image_name;
   //              $stmt = $this->con->prepare("INSERT INTO images (description, url) VALUES (?, ?)");
   //              $stmt->bind_param("ss", $uid, $name);
   //              if ($stmt->execute())
   //                  return $temp_array['profilePicUpdate'] = "success";
   //              return $temp_array['profilePicUpdate'] = "error";
   //             // return $temp_array['profilePicUpdate'] = "success";
   //         } else {
   //             return $temp_array['profilePicUpdate'] = "error";
   //         }
   //     } else {
   //         return 0;
   //     }
   // }

   public function updateprofilepic($uid,$profilepic,$com_name,$email) {
       $temp_array = array();
       if (is_uploaded_file($profilepic["tmp_name"])) {
           $tmp_file = $profilepic["tmp_name"];
           $image_name = $uid."_".time().'.png';
           // $upload_dir = './image/'.$image_name.'.png';
           $filedest = dirname(__FILE__) . UPLOAD_PATH . $image_name;
           if (move_uploaded_file($tmp_file,$filedest)) 
           {
                $name = "http://192.168.43.40:8081/ImageUploadApi/uploads/".$image_name;
                $stmt = $this->con->prepare("INSERT INTO images (description, url, complaintname, emailid) VALUES (?, ?, ?, ?)");
                $stmt->bind_param("ssss", $uid, $name, $com_name, $email);
                if ($stmt->execute())
                    return $temp_array['profilePicUpdate'] = "success";
                return $temp_array['profilePicUpdate'] = "error";
               // return $temp_array['profilePicUpdate'] = "success";
           } else {
               return $temp_array['profilePicUpdate'] = "error";
           }
       } else {
           return 0;
       }
   }
 
    // public function saveFile($file, $extension, $desc)
    // {
    //     $name = round(microtime(true) * 1000) . '.' . $extension;
    //     $filedest = dirname(__FILE__) . UPLOAD_PATH . $name;
    //     move_uploaded_file($file, $filedest);
 
    //     $url = $server_ip = gethostbyname(gethostname());
 
    //     $stmt = $this->con->prepare("INSERT INTO images (description, url) VALUES (?, ?)");
    //     $stmt->bind_param("ss", $desc, $name);
    //     if ($stmt->execute())
    //         return true;
    //     return false;
    // }

    public function saveFile($file, $extension, $desc, $com_name, $email)
    {
        $name = round(microtime(true) * 1000) . '.' . $extension;
        $filedest = dirname(__FILE__) . UPLOAD_PATH . $name;
        move_uploaded_file($file, $filedest);
 
        $url = $server_ip = gethostbyname(gethostname());
        //yaha par wahi name likhna bracket main jo columnn name hain
        $stmt = $this->con->prepare("INSERT INTO images (description, url, complaintname, emailid) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $desc, $name, $com_name, $email);
        if ($stmt->execute())
            return true;
        return false;
    }
 
    public function getAllFiles()
    {
        $stmt = $this->con->prepare("SELECT id, description, url FROM images ORDER BY id DESC");
        $stmt->execute();
        $stmt->bind_result($id, $desc, $url);
 
        $images = array();
 
        while ($stmt->fetch()) {
 
            $temp = array();
            $absurl = 'http://' . gethostbyname(gethostname()) . '/ImageUploadApi' . UPLOAD_PATH . $url;
            $temp['id'] = $id;
            $temp['desc'] = $desc;
            $temp['url'] = $absurl;
            array_push($images, $temp);
        }
 
        return $images;
    }
 
}