function search() {
	var search_str = document.getElementById("search-input").value;
	var posts = document.getElementsByClassName("post");

	Array.from(posts).forEach(function(post) {
		post.classList.remove("panel-success");
	});

	var found = false;

	Array.from(posts).forEach(function(post) {
		var text = post.getElementsByClassName("panel-body")[0].innerHTML;
		if (text.indexOf(search_str) != -1) {
			post.classList.add("panel-success");
			found = true;
		}
	});

	if (!found) {
		alert("Nothing found");
	}
}
