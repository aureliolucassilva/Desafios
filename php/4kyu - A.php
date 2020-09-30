//Link -> https://www.codewars.com/kata/52742f58faf5485cae000b9a

function format_duration($seconds) {
    $humanTime = [];
    $humanReadableTime = [];
    $time = "";

    if($seconds == 0) return "now";
  
    while($seconds > 0){
        if($seconds >= 365*24*60*60){
            $years = floor($seconds / (365*24*60*60));
            $humanTime['Y'] = $years;
            $seconds -= $years * (365*24*60*60);
        } else if($seconds >= 24*60*60){
            $days = floor($seconds / (24*60*60));
            $humanTime['D'] = $days;
            $seconds -= $days * (24*60*60);
        } else if($seconds >= 60*60){
            $hours = floor($seconds / (60*60));
            $humanTime['H'] = $hours;
            $seconds -= $hours * (60*60);
        } else if($seconds >= 60){
            $minutes = floor($seconds / 60);
            $humanTime['M'] = $minutes;
            $seconds -= $minutes * (60);
        } else{
            $humanTime['S'] = $seconds;
            $seconds = 0;
        }
    }

    foreach($humanTime as $key=>$value){
        switch($key){
            case "Y":
                if($value > 1) array_push($humanReadableTime, $value." "."years"); 
                else if($value == 1) array_push($humanReadableTime, "1 year");
                break;
            case "D":
                if($value > 1) array_push($humanReadableTime, $value." "."days"); 
                else if($value == 1) array_push($humanReadableTime, "1 day");
                break;
            case "H":
                if($value > 1) array_push($humanReadableTime, $value." "."hours"); 
                else if($value == 1) array_push($humanReadableTime, "1 hour");
                break;
            case "M":
                if($value > 1) array_push($humanReadableTime, $value." "."minutes"); 
                else if($value == 1) array_push($humanReadableTime, "1 minute");
                break;
            case "S":
                if($value > 1) array_push($humanReadableTime, $value." "."seconds"); 
                else if($value == 1) array_push($humanReadableTime, "1 second");
                break;
        }
    }

    for($i = 0; $i < sizeof($humanReadableTime); $i++) {
         switch($i){
            case sizeof($humanReadableTime) - 2:
                $time .= $humanReadableTime[$i]. " and ";
                break;
            case sizeof($humanReadableTime) - 1:
                $time .= $humanReadableTime[$i];
                break;
            default:
                $time .= $humanReadableTime[$i].", ";
          }
    }

    return $time;
}
