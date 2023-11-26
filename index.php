<?php
// index.php

$hugoContentDir = __DIR__ . '/hugo-cloudflare-build/content/posts/';

$backupDir = __DIR__ . '/post-backup/';

function getPosts() {
    global $hugoContentDir;

    $posts = [];
    $files = glob($hugoContentDir . '*');

    foreach ($files as $file) {
        $posts[] = pathinfo($file, PATHINFO_FILENAME);
    }

    return $posts;
}

function getPostContent($postSlug) {
    global $hugoContentDir;

    $postFile = $hugoContentDir . $postSlug . '.md';

    if (file_exists($postFile)) {
        return file_get_contents($postFile);
    }

    return false;
}

function savePostContent($postSlug, $title, $tags, $video_thumbnail, $video_url, $video_duration, $image, $images, $body, $description) {
    global $hugoContentDir, $backupDir;
	
    
	if($postSlug == '----'){
	   $postSlug = strtolower(str_replace(' ', '-', $title));
	}
    $postFile = $hugoContentDir . $postSlug . '.html';
	
	//do a backup
	file_put_contents($backupDir . $postSlug . '.html', file_get_contents($postFile));

    $content = "---\n";
    $content .= "title: \"$title\"\n";
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

function createNewPost() {
    global $hugoContentDir;

    $title = 'New Post';
    $postSlug = strtolower(str_replace(' ', '-', $title));

    $postFile = $hugoContentDir . $postSlug . '.md';

    if (!file_exists($postFile)) {
        $content = "---\n";
        $content .= "title: \"$title\"\n";
        $content .= "date: \"" . date("c") . "\"\n";
        $content .= "---\n\n";
        $content .= "Start writing your new post here.";

        if (file_put_contents($postFile, $content) !== false) {
            return $postSlug;
        }
    }

    return false;
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
	if(isset($_GET['slug'])){
		exit ( file_get_contents($hugoContentDir . $_GET['slug'] . '.html') );
		
	}
    $posts = getPosts();
    echo json_encode($posts);
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
?>
