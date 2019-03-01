<?php
//Course: cmps 4883
//Assignemt: A03
//Date: 3/1/2019
//Github username: 
//Repo url: 
//Name: Travis Bales
//Description: 
//    use sql database to get information scraped from nfl data and produce answers
//    using queries


//Connect to mysql
$host = "localhost";             // because we are ON the server
$user = "software_tools";        // user name

// Get username and password from slack
// The DB username and pass not the ones
// I sent you to log into the server.
$password = "**********";         // password 
$database = "nfl_data";              // database 
$mysqli = mysqli_connect($host, $user, $password, $database);

if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


/**
 * This function runs a SQL query and returns the data in an associative array
 * that looks like:
 * $response [
 *      "success" => true or false
 *      "error" => contains error if success == false
 *      "result" => associative array of the result
 * ]
 *
 */
function runQuery($mysqli,$sql){
    $response = [];

    // run the query
    $result = $mysqli->query($sql);

    // If we were successful
    if($result){
        $response['success'] = true;
        // loop through the result printing each row
        while($row = $result->fetch_assoc()){
            $response['result'][] = $row;
        }
        $result->free();
    }else{
        $response['success'] = false;
        $response['error'] = $mysqli->error;
    }

    return $response;
}


/**
 * Pulls a player out of players table and returns:
 *     [name] => Player.Name
 * Params:
 *     playerId [string] : id of type => 00-000001234
 * Returns:
 *     name [string] : => T. Smith
 */
function getPlayer($playerId){
    global $mysqli;
    $sql = "SELECT `name` FROM players WHERE id = '{$playerId}' LIMIT 1";
    $response = runQuery($mysqli,$sql); 
    if(!array_key_exists('error',$response)){
        return $response['result'][0]['name'];
    }
    return null;
}


/**
 * Prints a question plus a border underneath
 * Params:
 *     question [string] : "Who ran the most yards in 2009?"
 *     pads [array] : [3,15,15,5] padding for each data field
 * Returns:
 *     header [string] : Question with border below
 */
function printHeader($question,$pads,$cols){
    if(strlen($question) > array_sum($pads)){
        $padding = strlen($question);
    }else{
        $padding = array_sum($pads);
    }
    $header = "\n<b>";
    $header .= "{$question}\n\n";
    for($i=0;$i<sizeof($cols);$i++){
        $header .= str_pad($cols[$i],$pads[$i]);
    }
    $header .= "\n".str_repeat("=",$padding);
    $header .= "</b>\n";
    return $header;
}


/**
 * formatRows:
 *    Prints each row with a specified padding for allignment
 * Params:
 *    $row [array] - array of multityped values to be printed
 *    $cols [array] - array of ints corresponding to each column size wanted
 * Example:
 *    
 *    $row = ['1','00-00000123','T. Smith','329']
 *    $pads = [4,14,20,5]
 */
function formatRows($row,$pads){
    $ouput = "";
    for($i=0;$i<sizeof($row);$i++){
        $output .= str_pad($row[$i],$pads[$i]);
    }
    return $output."\n";
}



/**
 * displayQuery: print question + sql result in a consistent and 
 *               formatted manner
 * Params: 
 *     question [string] : question text
 *     sql [string] : sql query
 *     cols [array] : column headers in array form
 *     pads [array] : padding size in ints for each column
 */
function displayQuery($question,$sql,$cols,$pads){
    global $mysqli;
    $parts = explode('.',$question);
    if($parts[0]%2==0){
        $color="#C0C0C0";
    }else{
        $color = "";
    }
    echo"<pre style='background-color:{$color}'>";
    echo printHeader($question,$pads,$cols);
    $response = runQuery($mysqli,$sql);
    if($response['success']){
        foreach($response['result'] as $id => $row){
            $id++;
            $row['id'] = $id;
            $row['name'] = getPlayer($row['playerid']);
            $row[0] = $row[$cols[0]];
            $row[1] = $row[$cols[1]];
            $row[2] = $row[$cols[2]];
            $row[3] = $row[$cols[3]];
            echo formatRows($row,$pads);
        }
    }
    echo"</pre>";
    f();
}






echo"</pre>";
echo("Name: Travis Bales
Assignment: A04 - Nfl Stats 
Date: 3/1/2019

==================================================================================");
 /**
 * Question 10
 * Rank the NFL by win loss percentage (worst first).
 */
//Return 5 if the condition is TRUE, or 10 if the condition is FALSE:
//SELECT IF(500<1000, 5, 10);
$question = "10. Rank the NFL by win loss percentage (worst first).";
$pads = [3,5,15];
$sql = "SELECT `club`, sum(if(`wonloss` = @won,1,0))/ sum(if(`wonloss` = @loss,1,0)) as total 
        FROM `game_totals` 
        GROUP BY `club` 
        ORDER BY total ASC
        LIMIT 5
";
$response = runQuery($mysqli, $sql);
$cols = ['id','club','total'];
displayQuery($question,$sql,$cols,$pads);









