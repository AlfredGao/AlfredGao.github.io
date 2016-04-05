<?php
  header('Access-Control-Allow-Origin: *');
?>
<?php
	if(isset($_GET['input'])){
		$lookup = "http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input={$_GET['input']}";
		$contents = file_get_contents($lookup);
		echo $contents;
	}
?>
<?php
	if(isset($_GET['symbol'])){
        $quote = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol={$_GET['symbol']}";
        $contents = file_get_contents($quote);
        echo $contents;
    }

?>


<?php

	if(isset($_GET['symbol_name'])){

		$accountKey = '+gV3zr+J52Qy4lWnTaB/Cnw9zqCyiqWFaaXh23Pzubg';
		$ServiceRootURL =  'https://api.datamarket.azure.com/Bing/Search/';
        $WebSearchURL = $ServiceRootURL.'News?$format=json&Query=';
        $new = $WebSearchURL.'\''.$_GET['symbol_name'].'\'';
        //echo $new;
		$context = stream_context_create(array(
    		'http' => array(
        	'request_fulluri' => true,
        	'header'  => "Authorization: Basic " . base64_encode($accountKey . ":" . $accountKey)
    			)
		));
		$contents = file_get_contents($new,0,$context);
		echo $contents;
	}
?>