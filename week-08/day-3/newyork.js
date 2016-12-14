let xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecf5a7de7cc04cb2b96621ac0933ae26&q=apollo11 landing', true);
xhr.send(null);
xhr.onreadystatechange = ready

function ready(rsp) {
	if( xhr.readyState === XMLHttpRequest.DONE ) {
		var apolloArticles = JSON.parse(xhr.response);
    console.log(apolloArticle);
    display(apolloArticles);
	}
}

fuction display(apolloArticles){
  ``
}
