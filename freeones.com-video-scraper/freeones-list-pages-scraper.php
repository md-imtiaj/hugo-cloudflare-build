<?php
//$htmlContent = file_get_contents('tmp2.html');

if(isset($_GET['p'])){ $p = $_GET['p']; }
else{ $p = 1; }

$proxy = "https://script.google.com/macros/s/AKfycbytIJNJ-x8iGHHN8AgxoVa60Z1HWJorMiOyPyA4eUIYbAsZdbpMJj8eJErevCVviJdTNQ/exec?url=https://www.freeones.com/videos?p=$p";

$htmlContent1 = file_get_contents($proxy);
$json_data1 = json_decode($htmlContent1, true);
$htmlContent = $json_data1 ['data'];

//file_put_contents('ttt.html', $htmlContent);
// Suppress errors related to SVG tags
libxml_use_internal_errors(true);

$dom = new DOMDocument();
$dom->loadHTML($htmlContent);

$teaserVideoDivs = $dom->getElementsByTagName('div');
$counter = 1;
foreach ($teaserVideoDivs as $div) {
    if ($div->getAttribute('data-test') == 'teaser-video') {
		$a = $div->getElementsByTagName('a')->item(0);
		if ($a) {			
            // Extract title, image source (src)
            $link = 'https://www.freeones.com' . $a->getAttribute('href');
			echo "$counter. <a href='http://localhost:85/freeones-video-pages-info-scraper.php?url=$link' target='_blank'>$link</a>";
			echo "<br>\n";
			$counter = $counter + 1;
		}
		//trailer webm
		$img = $div->getElementsByTagName('img')->item(0);
		if ($img) {			
            // Extract 
            $trailer_url = $img->getAttribute('data-media') . 'WebM.webm';
			echo " Trailer: <a href='$trailer_url' target='_blank'>$trailer_url</a>";
			echo "<br><br>\n";
		}
		
	}
}