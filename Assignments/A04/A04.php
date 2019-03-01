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
 * Question 1
 * Count number of teams an individual player played for.
 */
$question = "1. Find the player(s) that played for the most teams.";
$pads = [3,20,17,5];
$sql = "SELECT id as playerid,name,count(distinct(club)) as count 
        FROM `players` 
        group by id,name 
        ORDER BY `count` DESC 
        LIMIT 10";
$cols = ['id','name','count'];
displayQuery($question,$sql,$cols,$pads);
/**
 * Question 2
 * Find the players with the highest total rushing yards by year, and limit the result to top 5.
 */
$question = "2. Find the players with the highest total rushing yards by year, and limit the result to top 5.";
$pads = [3,12,12,5];
$sql = "SELECT `players_stats`.`season` as year,`players_stats`.`playerid` as playername,
        sum(`players_stats`.`yards`) as total
        FROM `players_stats`
        Where `players_stats`.`statid` = 10
        GROUP BY year,playername
        ORDER BY total DESC
        LIMIT 5";
$cols = ['id','playername','year','total'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 3
 * Find the bottom 5 passing players per year.
 */
$question = "3. Find the bottom 5 passing players per year.";
$pads = [3,12,17,17,17];
$sql = "SELECT `season`,`playerid`,
sum(`players_stats`.`yards`) as total
FROM `players_stats`
Where `players_stats`.`statid` = 15
GROUP BY `season`,`playerid`
ORDER BY total ASC
LIMIT 5";
$cols = ['#','playerid','name','season','negative_carries'];
displayQuery($question,$sql,$cols,$pads);


 /**
 * Question 4
 * Find the top 5 players that had the most rushes for a loss.
 */
$question = "4. Find the top 5 players that had the most rushes for a loss.";
$pads = [3,12,18,5];
$sql = "SELECT `playerid`,sum(`yards`) as negative_yards 
        FROM `players_stats` 
        WHERE `yards` < 0 and `statid` = 10 
        GROUP BY `playerid` 
        ORDER BY negative_yards ASC
        LIMIT 5";
$cols = ['id','name','negative_yards'];
displayQuery($question,$sql,$cols,$pads);

 /**
 * Question 5
 * Find the top 5 teams with the most penalties.
 */
$question = "5. Find the top 5 teams with the most penalties.";
$pads = [5,5];
$sql = "SELECT club,sum(pen) as pen 
        FROM `game_totals` 
        GROUP BY club  
        ORDER BY `pen`  DESC
        LIMIT 5";
$cols = ['club','pen'];
displayQuery($question,$sql,$cols,$pads);

 /**
 * Question 6
 * Find the average number of penalties per year.
 */
$question = "6. Find the average number of penalties per year.";
$pads = [3,8,15,17];
$sql = "SELECT `season`, sum(`pen`) as total, avg(`pen`) as avg 
        FROM `game_totals` 
        GROUP BY `season`
        LIMIT 5";
$response = runQuery($mysqli, $sql);
$cols = ['id','season','total','avg'];
displayQuery($question,$sql,$cols,$pads);

 /**
 * Question 7
 * Find the Team with the least amount of average plays every year.
 */
$question = "7. Find the Team with the least amount of average plays every year.";
$pads = [8,15,15];
$sql = "SELECT `clubid`,`gameid`,`playid`,COUNT(`playid`) as total FROM `plays` GROUP BY `clubid` ORDER BY total ASC LIMIT 5";
$response = runQuery($mysqli, $sql);
$cols = ['clubid','gameid','total'];
displayQuery($question,$sql,$cols,$pads);
 /**
 * Question 8
 * Find the top 5 players that had field goals over 40 yards.
 */
$question = "8. Find the top 5 players that had field goals over 40 yards.";
$pads = [3,12,15];
$sql = "SELECT `playerid`,`yards`
        FROM `players_stats`
        WHERE `statid` = 70
        AND `yards` > 40
        GROUP BY `playerid`
        ORDER BY 'yards' DESC
        LIMIT 5
";
$response = runQuery($mysqli, $sql);
$cols = ['id','playerid','yards'];
displayQuery($question,$sql,$cols,$pads);

 /**
 * Question 9
 * Find the top 5 players with the shortest avg field goal length.
 */
$question = "9. Find the top 5 players with the shortest avg field goal length.";
$pads = [3,15,8];
$sql = "SELECT `playerid`, avg(`players_stats`.`yards`) as averageyrds
        FROM `players_stats`
        WHERE `statid` = 70
        GROUP BY `players_stats`.`playerid`
        ORDER BY averageyrds ASC
        LIMIT 5";
$response = runQuery($mysqli, $sql);
$cols = ['id','playerid','averageyrds'];
displayQuery($question,$sql,$cols,$pads);
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

/**
 * Question 11
 * Find the top 5 most common last names in the NFL.
 */
$question = "11. Find the top 5 most common last names in the NFL.";
$pads = [3,15,12];
$sql = "SELECT `name` as person, COUNT(*)as total 
        FROM `players` 
        GROUP BY `person` 
        ORDER BY total DESC, person
        LIMIT 5";
$response = runQuery($mysqli, $sql);
$cols = ['id','person','total'];
displayQuery($question,$sql,$cols,$pads);
