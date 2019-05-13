<?php
function dd($value) {
    echo "<pre>";
    var_dump($value);
    echo "</pre>";
}
error_reporting(E_ALL);
ini_set("display_errors", "on");
echo $_SERVER['REQUEST_METHOD'];
// echo $_SERVER['REQUEST_URL'];
$route = explode('/', $_SERVER['REQUEST_URI']);
switch($_SERVER["REQUEST_METHOD"]){
case 'POST':{
    if ($route[2] == 'signup') {
        signup();
    } else if ($route[2] == 'close') {
        close();
    } else {
        //TODO
    }
    break;
}
case 'GET':
    getUserInfo($route[3]);
    break;
case 'PATCH':
    updateUserInfo();
    break;
}

function signup() {
    echo 'may!!! post!!';
    $resource = file_get_contents('php://input');
    $data = json_decode($resource);
    $fileData = json_decode(file_get_contents('./info.txt'));
    if (isset($fileData[$data['user_id']])) {
        $res = [
            'message' => 'Account creation failed',
            'cause' => 'already same user_id is used'
        ];
    } else {
        $fileData[$data['user_id']] = $data['password'];
        file_put_contents('./info.txt', json_encode($fileData));
        $res = [
            'message' => 'Account successfully created',
            'user' => [
                'user_id' => $data['user_id'],
                'nickname' => $data['user_id']
            ]
        ];
        echo json_encode($res);
        exit;
    }
}

function close() {
}

function getUserInfo($userId) {
    $fileData = json_decode(file_get_cntents('./info.text'));

}

function updateUserInfo() {
}
