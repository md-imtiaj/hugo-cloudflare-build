<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hugo Content Editor</title>
	<!--script src="https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.0.0/js-yaml.min.js"></script-->
	<script src="<?php echo $adminSrcDir; ?>/assets/js-yaml.min.js"></script>
	
	<!--link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"-->
	<link rel="stylesheet" href="<?php echo $adminSrcDir; ?>/assets/water.css">
	
    <!--link href="https://cdn.jsdelivr.net/npm/froala-editor@latest/css/froala_editor.pkgd.min.css" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/froala-editor@latest/js/froala_editor.pkgd.min.js"></script-->
	
	<!--script src="https://cdn.ckeditor.com/4.22.1/standard/ckeditor.js"></script-->
	<script src="<?php echo $adminSrcDir; ?>/ckeditor/ckeditor.js"></script>
	
	

	
<style>
	 body{max-width: 950px;}
	 
 /* Style for the custom alert */
	#custom-alert {
		display: none;
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		padding: 20px;
		background-color: #fff;
		border: 1px solid #ccc;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
		z-index: 1000;
	}
	
	red {
      color: red;
      font-size: 1.2em; /* Adjust the font size as needed */
    }
	red::before {
      content: '*';
      color: red;
    }
	
	 .char-counter {
      color: green;
    }

    .char-warning {
      color: red;
    }
</style>
</head>
<body>
    <label for="post-list">Create New Post or Select to Edit:</label>
    <select id="post-list"></select>
	

    <label for="post-title" >Title:<red></label>
    <input type="text" id="post-title" size="122px" value="<?php echo $title; ?>" placeholder="Post title, will use as post slug if new, if edit title will change but slug remains same." required>
	
	<label for="post-slug">Post Slug:</label>
    <input type="text" id="post-slug" size="122px" placeholder="Post slug will be generated">


	<label for="post-title">Description:<red></label>
    <textarea  id="post-description" placeholder="Excerpt: meta tag description, Important for seo!!!" rows="2" required><?php echo $description; ?></textarea>
	<div >Characters left: <span id="char-counter" class="char-counter">170</span></div><br/>

    <label for="post-tags">Tags (comma-separated):<red></label>
    <input type="text" id="post-tags" size="122px" value="<?php echo $tags; ?>" placeholder="At least add main tags i.e pornstar, video, photos, indian" required>
	
	
	<label for="post-video-thumbnail">Video Poster:</label>
    <input type="text" id="post-video-thumbnail" size="122px" value="<?php echo $poster; ?>" placeholder="This will show as video poster.">
	<img id="post-video-thumbnail-preview" src="<?php echo "http://i0.wp.com/" . @preg_replace("~^(?:f|ht)tps?://~i", "", $poster); ?>" height="150px" width="200px" <?php if($poster=='') echo "style='display:none;'"; ?>/><br/>
	
	<label for="post-video">Video Url:</label>
    <input type="text" id="post-video" size="122px" value="<?php echo $video_url; ?>" placeholder="Direct link of the source .mp4 video.">
	
	<label for="post-video-duration">Video Duration:</label>
    <input type="text" id="post-video-duration" size="122px" value="<?php echo $duration; ?>" placeholder="Video duration like 5:09">

    <label for="post-image">Feature Image:<red></label>
    <input type="text" id="post-image" size="122px" placeholder="Top image for posts and Thumbnail for videos. Must add" required>
	<img id="post-image-preview" src="" height="150px" width="200px" style='display:none;'/><br/>

	
	<label for="post-images">Images (comma-separated):</label>
    <input type="text" id="post-images" size="122px" placeholder="Images comma separated, will add in image SiteMap">

    <label for="post-body">Post Body:<red></label>
    <textarea id="post-body" placeholder="Start writing here." rows="20" required></textarea>

    <!--button id="new-post-btn">Create New Post</button-->
    <br/><button id="save-btn">Save</button>


<!-- Custom alert container -->
<div id="custom-alert">
    <p id="alert-message"></p>
    <button onclick="closeCustomAlert()">OK</button>
</div>


    <script>
	    var postSlugEditLock = false;
		
		var ckeditor = CKEDITOR.replace( 'post-body', {
			height: 600
		});
		
        //DOMContentLoaded is used to load the ckeditor first and then do other things.	
        document.addEventListener('DOMContentLoaded', function() {
            const postList = document.getElementById('post-list');
            const newPostBtn = document.getElementById('new-post-btn');
			
			

            function loadPostList() {
                fetch('?list-posts=true')
                    .then(response => response.json())
                    .then(posts => {
                        
						//add the default New Post item.
						const option = document.createElement('option');
						option.value = 'new-post';
						option.text = 'New Post';
						postList.add(option);
						
						//now add all the existing posts for editing
                        posts.forEach(post => {
                            const option = document.createElement('option');
                            option.value = post;
                            option.text = post;
                            postList.add(option);
                        });

                       						
						//load a blank post (New Post)
						CKEDITOR.instances['post-body'].setData('<h1 class="mb-4">Post Title</h1><p class="lead">A brief excerpt or summary of your post goes here.</p><div class="row mt-4"><div classs="col-md-8"><h2>Image Title</h2><img src="<?php echo $adminSrcDir; ?>/assets/<?php echo $adminSrcDir; ?>-sample.jpg" alt="Image" class="img-fluid mb-3"><p class="text-muted">Image Label</p></div></div>');
                    });
            }

            function loadPostContent(postSlug) {
				console.log('Post slug: ', postSlug);
				postSlugEditLock = true;
                fetch(`?slug=${postSlug}`)
                    .then(response => response.text())
                    .then(content => {//console.log(content)
                        const frontmatter = content.split('---\n')[1];
                        const data = jsyaml.load(frontmatter);

                        document.getElementById('post-title').value = data.title || '';
						
                        document.getElementById('post-slug').value = data.slug || '';
                        document.getElementById('post-slug').readOnly  = true;
						
                        document.getElementById('post-description').value = data.description || '';
						//adjust text area height
						adjustTextareaHeight(document.getElementById('post-description'));
						
						document.getElementById('post-tags').value = data.tags ? data.tags.join(', ') : '';
						
                        document.getElementById('post-video-thumbnail').value = data.video ? data.video.image : '';
                        document.getElementById('post-video').value = data.video ? data.video.url : '';
                        document.getElementById('post-video-duration').value = data.video ? data.video.duration : '';
						
						document.getElementById("post-video-thumbnail-preview").src = data.video ? data.video.image : '';
						console.log('src',document.getElementById("post-video-thumbnail-preview").src);
						if(data.video ? data.video.image : '' !=''){
						  document.getElementById("post-video-thumbnail-preview").style.display = "inline";
						}
						
						
                        document.getElementById('post-image').value = data.image || '';                        
                        document.getElementById('post-images').value = data.images ? data.images.join(', ') : '';
						
						document.getElementById("post-image-preview").src = data.image || ''; 
						if(data.image || '' != ''){
						  document.getElementById("post-image-preview").style.display = "inline";
						}
						
										   
                        //document.getElementById('post-body').value = content.split('---\n').slice(2).join('---\n');
						CKEDITOR.instances['post-body'].setData(content.split('---\n').slice(2).join('---\n'));
						
                    });
            }

           
            loadPostList();

            postList.addEventListener('change', function() {
                const selectedPost = this.value;
                loadPostContent(selectedPost);
            });

            //newPostBtn.addEventListener('click', createNewPost);

            document.getElementById('save-btn').addEventListener('click', function() {
                const selectedPost = postList.value;
                const title = document.getElementById('post-title').value;
                const slug = document.getElementById('post-slug').value;
                const description = document.getElementById('post-description').value;
                const tags = document.getElementById('post-tags').value;
				
                const video_thumbnail = document.getElementById('post-video-thumbnail').value;
                const video_duration = document.getElementById('post-video-duration').value;
                const video_url = document.getElementById('post-video').value;
				
                const image = document.getElementById('post-image').value;
                const images = document.getElementById('post-images').value;
                //const body = document.getElementById('post-body').value; console.log(body);
                const body =  CKEDITOR.instances['post-body'].getData();
				
				if(title=='' || description=='' || tags=='' || body==''){
					alert("<span style='color:red;'>Fields with red asterisk are required.</span>");
					return;
				}

                fetch('', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `action=save&slug=${slug}&title=${encodeURIComponent(title)}&tags=${encodeURIComponent(tags)}&video_thumbnail=${encodeURIComponent(video_thumbnail)}&video_duration=${encodeURIComponent(video_duration)}&video_url=${encodeURIComponent(video_url)}&image=${encodeURIComponent(image)}&images=${encodeURIComponent(images)}&body=${encodeURIComponent(body)}&description=${encodeURIComponent(description)}`,
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Content saved successfully!');
                    } else {
                        alert('Failed to save content.');
                    }
                });
            });
        });
    </script>
	
<script>
    // Function to show custom alert
    function showCustomAlert(message) {
        // Set the alert message
        document.getElementById('alert-message').innerHTML = message;

        // Display the custom alert
        document.getElementById('custom-alert').style.display = 'block';
    }

    // Function to close custom alert
    function closeCustomAlert() {
        // Hide the custom alert
        document.getElementById('custom-alert').style.display = 'none';
    }

    // Replace the default alert function with the custom alert
    window.alert = showCustomAlert;

    // Example usage
    //alert('This is a custom alert!');

</script>

<script>
        // Function to generate slug from title
        function generateSlug() {
		 if(!postSlugEditLock){
            var title = document.getElementById('post-title').value;
            var slug = title.toLowerCase().replace(/[^a-z0-9 -]/g, '').replace(/\s+/g, '-');
            document.getElementById('post-slug').value = slug;
			}
        }

        // Attach the function to the 'input' event of the title input
        document.getElementById('post-title').addEventListener('input', generateSlug);
   
</script>


<script>
  /*post image preview with post image input change*/
  document.addEventListener("DOMContentLoaded", function() {
    // Get references to the input and image elements
    var postImageInput = document.getElementById("post-image");
    var postImagePreview = document.getElementById("post-image-preview");

    // Listen for input change event
    postImageInput.addEventListener("input", function() {
      // Update the src attribute of the image preview
      var inputValue = postImageInput.value;
      postImagePreview.src = inputValue;

      // Show the image preview if there's a value, otherwise hide it
      if (inputValue) {
        postImagePreview.style.display = "inline"; // Show the image
      } else {
        postImagePreview.style.display = "none"; // Hide the image
      }
    });
  });
</script>





<script>
  /*post-video-thumbnail-preview with post post-video-thumbnail change*/
  document.addEventListener("DOMContentLoaded", function() {
    // Get references to the input and image elements
    var postImageInput = document.getElementById("post-video-thumbnail");
    var postImagePreview = document.getElementById("post-video-thumbnail-preview");

    // Listen for input change event
    postImageInput.addEventListener("input", function() {
      // Update the src attribute of the image preview
      var inputValue = postImageInput.value;
      postImagePreview.src = inputValue;

      // Show the image preview if there's a value, otherwise hide it
      if (inputValue) {
        postImagePreview.style.display = "inline"; // Show the image
      } else {
        postImagePreview.style.display = "none"; // Hide the image
      }
    });
  });
</script>

<script>


// Function to adjust the textarea height based on content
  function adjustTextareaHeight(descriptionTextarea) {
    // Set a minimum number of rows (e.g., 1)
    var minRows = 1;

    // Calculate the number of rows based on the content
    var currentRows = minRows + Math.floor((descriptionTextarea.scrollHeight - descriptionTextarea.clientHeight) / 10); // Adjust the divisor as needed

    // Update the rows attribute
    descriptionTextarea.rows = currentRows;
  }

 
</script>


<script>
    // Get the textarea element
    var descriptionInput = document.getElementById('post-description');

    // Get the counter element
    var charCounter = document.getElementById('char-counter');

    // Set the maximum number of characters
    var maxChars = 170;
    var alertThreshold = 120;

    // Add an input event listener to the textarea
    descriptionInput.addEventListener('change', calculateChars);
    descriptionInput.addEventListener('input', calculateChars);
	
	function calculateChars() {
      // Get the current number of characters
      var currentChars = descriptionInput.value.length;

      // Update the counter
      charCounter.textContent = (maxChars - currentChars) + '/170. Total Characters: ' + currentChars;

      // Change text color to red if reaching the alert threshold
      if (currentChars > alertThreshold) {console.log('ok')
        charCounter.classList.add('char-warning');
		charCounter.classList.remove('char-counter');
      } else {
        charCounter.classList.remove('char-warning');
		charCounter.classList.add('char-counter');
      }
	  
	  if (currentChars > maxChars) {
        alert("Chars exceeded maximum Threshold of 170 Chars.");
      } 
    }
</script>
  
  
</body>
</html>
