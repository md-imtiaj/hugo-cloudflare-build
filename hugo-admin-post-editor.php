<?php

$adminSrcDir = 'hugo-admin-post-editor';

$hugoContentFolder = "content/posts";
$hugoContentVideosFolder = "content/videos";
$hugoContentDir = __DIR__ . "/$hugoContentFolder/";

$backUpFolderName = "posts-backup";
$backupDir = __DIR__ . "/$backUpFolderName/";



// Check if the folder exists
if (!is_dir($backUpFolderName)) {
    // Create the folder if it doesn't exist
    mkdir($backUpFolderName);
} 

if (!is_dir($hugoContentFolder)) {
    mkdir($hugoContentFolder, 0777, true); // The third parameter (true) creates parent directories if they don't exist
} 

if (!is_dir($hugoContentVideosFolder)) {
    mkdir($hugoContentFolder, 0777, true); // The third parameter (true) creates parent directories if they don't exist
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
	/*Get the args*/
	$title = @$_GET['title'];
	$description = @$_GET['description'];
	$tags = @$_GET['tags'];
	$poster = @$_GET['poster'];
	$video_url = @$_GET['video_url'];
	$duration = @$_GET['duration'];
	
	
	
	if(isset($_GET['slug'])){
		exit ( file_get_contents($hugoContentDir . $_GET['slug'] . '.html') );
		
	}
	else if(isset($_GET['list-posts'])){
      $posts = getPosts();
      echo json_encode($posts);
	}
	else{
	  require_once("$adminSrcDir/editor.php");
    }
	
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];

    if ($action === 'create') {
        $newPostSlug = createNewPost();
        echo json_encode(['slug' => $newPostSlug]);
		
    } elseif ($action === 'save') {
        //echo '<script>';
        //echo 'var postData = ' . json_encode($_POST) . ';';
        //echo '</script>';
        $postSlug = $_POST['slug'];
        $title = $_POST['title'];
        $description = $_POST['description'];
        $tags = $_POST['tags'];
		
		$video_thumbnail = $_POST['video_thumbnail'];
		$video_url = $_POST['video_url']; 
		$video_duration = $_POST['video_duration'];
		
        $image = $_POST['image'];
        $images = $_POST['images'];
        $body = $_POST['body'];
		

        if (savePostContent($postSlug, $title, $tags, $video_thumbnail, $video_url, $video_duration, $image, $images, $body, $description)) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false]);
        }
    }
}



function getPosts() {
    global $hugoContentDir;

    $posts = [];
    $files = glob($hugoContentDir . '*');
	
	//get only last 100 files
	// Sort the files based on their creation time in descending order (newest first)
	usort($files, function ($a, $b) {
		return filectime($b) - filectime($a);
	});

    // Get the last 100 files
    $last100Files = array_slice($files, 0, 100);

    foreach ($last100Files as $file) {
        $posts[] = pathinfo($file, PATHINFO_FILENAME);
    }

    return $posts;
}


function savePostContent($postSlug, $title, $tags, $video_thumbnail, $video_url, $video_duration, $image, $images, $body, $description) {
    global $hugoContentDir, $backupDir;
	
    
	if($postSlug == 'new-post'){
	   $postSlug = strtolower(str_replace(' ', '-', $title));
	}
    $postFile = $hugoContentDir . $postSlug . '.html';
	
	//do a backup
	file_put_contents($backupDir . $postSlug . '.html', @file_get_contents($postFile));

    $content = "---\n";
    
	if($video_thumbnail != '' && $video_url!=''){
		$content .= "title: \"$title Video\"\n";
	}
	else{
		$content .= "title: \"$title\"\n";
	}
	
    $content .= "slug: \"$postSlug\"\n";
	
	if($video_thumbnail != '' && $video_url!=''){
		$content .= "url: \"video/$postSlug\"\n";
	}
	
    $content .= "description: \"$description\"\n";
    $content .= "date: \"" . date("c") . "\"\n";
    $content .= "tags: [" . implode(', ', array_map('trim', explode(',', $tags))) . "]\n";
    $content .= "image: " . "\"$image\"\n";
    $content .= "images: [" . implode(', ', array_map('trim', explode(',', $images))) . "]\n";
	
	if($video_thumbnail != '' && $video_url!=''){
		$content .= "video: \n url: \"$video_url\" \n duration: \"$video_duration\" \n image: \"$video_thumbnail\" \n";
		
	}
    $content .= "---\n\n";
    $content .= $body;

    if (file_put_contents($postFile, $content) !== false) {
        return true;
    }

    return false;
}