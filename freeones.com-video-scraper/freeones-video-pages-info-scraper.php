<?php
//$htmlContent = file_get_contents('tmp2.html');


if(isset($_GET['url'])){ $url = $_GET['url']; }
else(die("Please provide a frreones.com video url."));

$proxy = "https://script.google.com/macros/s/AKfycbytIJNJ-x8iGHHN8AgxoVa60Z1HWJorMiOyPyA4eUIYbAsZdbpMJj8eJErevCVviJdTNQ/exec?url=$url";

$htmlContent1 = file_get_contents($proxy);
$json_data1 = json_decode($htmlContent1, true);
$htmlContent = $json_data1 ['data'];

// Suppress errors related to SVG tags
libxml_use_internal_errors(true);

$dom = new DOMDocument();
$dom->loadHTML($htmlContent);

$ldJson = $dom->getElementsByTagName('script');
foreach ($ldJson as $lj) {
    if ($lj->getAttribute('type') == 'application/ld+json') {
		//print_r(json_decode($div->nodeValue, true)); 
		$json_data = json_decode($lj->nodeValue, true); 
		if($json_data['@type'] == 'VideoObject') {
			//print_r($json_data);
			$title = $json_data['name'];
			echo "<b>Title: </b> $title<br/>\n";
			$durationString = $json_data['duration'];
			echo "<b>Duration String: </b> $durationString<br/>\n";

// Check if the duration string already starts with 'P'
if (substr($durationString, 0, 1) !== 'P') {
    // If not, add 'P' to the duration string
    $durationString = 'P' . $durationString;
}

// Create a DateInterval object from the corrected duration string
$interval = new DateInterval($durationString);

// Calculate the total number of seconds
$totalSeconds = $interval->s + ($interval->i * 60) + ($interval->h * 3600);

// Format the seconds into h:m:s without any separators or leading zeros for hours
$formattedTime = @ltrim(sprintf('%d:%02d:%02d', ($totalSeconds / 3600), ($totalSeconds / 60 % 60), $totalSeconds % 60), '0:');

echo "<b>Duration formatted: </b> $formattedTime<br/>\n";

$duration = $formattedTime;

			echo "<br/>\n";
			$poster = $thumbnailUrl = $json_data['thumbnailUrl'];
			echo "<b>Poster Url: </b> $poster<br/>\n";
			$video_url = $contentUrl = $json_data['contentUrl'];
			echo "<b>Video Mp4 Url: </b> $video_url<br/>\n";
		}
	}
}

//description
$divs = $dom->getElementsByTagName('div');
$description = '';
foreach ($divs as $div) {
    if ($div->getAttribute('class') == 'common-text mb-2') {
		$description = @trim($div->nodeValue);
		if ($description !=''){ $description = $description . ','; }
		echo "<b>Description: </b> $description<br/>\n";
	}
}

//tags
echo "\n\n\n";
$tags = array();
foreach ($divs as $div) {
    if ($div->getAttribute('class') == 'badge-scroll') {
		$hrefs = $div->getElementsByTagName('a');
		foreach ($hrefs as $href) {
			if ($href->getAttribute('class') == 'badge badge-xs px-2 badge-secondary font-size-xs' || $href->getAttribute('class') == 'badge badge-xs  px-2 badge-secondary  font-size-xs js-event') {
				$tag = trim($href->nodeValue);
				$tags[] =  $tag;
			}
		}
	}
}

$tags = array_unique($tags);
$tags = implode(',',$tags);

echo "<br/>\n<b>Tags: </b> $tags<br/>\n";

//echo $prompt = "Describe a porn scene about $title. $description. include the $tags keywords.";



$prompt = "Craft authentic and emotionally rich porn video scene descriptions that resonate with human experiences. Leverage the $title, $description include the $tags keywords to create narratives that not only inform but also connect with the audience on a personal level. Imbue the text with a genuine and relatable tone, capturing the essence of the content in a way that sparks curiosity, excitement, or any relevant emotions. Make the descriptions feel as though they were written by a person, incorporating warmth, enthusiasm, and a touch of personality.";

echo "<br/><br/><textarea rows=15 cols=90 onclick=\"copyText()\" id=\"myTextarea\">$prompt</textarea><br/><br/>";
?>

<script>
	let myWindow;
	
	let editor_url = 'http://localhost/hugo-admin-post-editor.php?title=' + encodeURIComponent('<?php echo rawurldecode(addslashes($title)); ?>') + '&description=' + encodeURIComponent('<?php echo rawurldecode(addslashes($description)); ?>') + '&tags=' + encodeURIComponent('<?php echo $tags; ?>') + '&poster=' + encodeURIComponent('<?php echo $poster; ?>') + '&video_url=' + encodeURIComponent('<?php echo $video_url; ?>') + '&duration=' + encodeURIComponent('<?php echo $duration; ?>');

	function openOrReloadWindow() {
		if (myWindow && !myWindow.closed) {
			// Reload the existing window with new arguments
			myWindow.location.href = editor_url;
		} else {
			// Open a new window with the specified arguments
			myWindow = window.open(editor_url, '_blank');
		}
	}
</script>

<script>
        function copyText() {
            // Get the textarea element
            var textarea = document.getElementById("myTextarea");

            // Select the text inside the textarea
            textarea.select();

            // Copy the selected text to the clipboard
            document.execCommand("copy");

            // Deselect the text
            textarea.setSelectionRange(0, 0);

            // Alert the user that the text has been copied (optional)
            alert("Text copied to clipboard!");
        }
    </script>


<a href="javascript:void(0);" onclick="openOrReloadWindow()">Put in Editor</a>