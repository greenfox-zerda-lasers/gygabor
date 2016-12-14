let xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecf5a7de7cc04cb2b96621ac0933ae26&q=apollo11 landing', true);
xhr.send(null);
xhr.onreadystatechange = ready

function ready(rsp) {
	if( xhr.readyState === XMLHttpRequest.DONE ) {
		var apolloArticles = JSON.parse(xhr.response);
    appendList();
    display(apolloArticles.response.docs);
	}
}

function appendList(){
  var artList = document.querySelector('section')
  var list = document.createElement('dl');
  list.id = 'article-list';
  artList.appendChild(list);
}

function display(apolloArt){
  apolloArt.forEach(function(article){
    console.log(article)
    var listheadline = document.createElement('dt');
    listheadline.innerText = 'Headline: '+ article.headline.main;
    var artlist = document.querySelector('#article-list');
    artlist.appendChild(listheadline);

    var snippet = document.createElement('dd');
    snippet.innerText = 'Snippet: '+ article.snippet;
    artlist.appendChild(snippet);
    var date = document.createElement('dd');
    date.innerText = 'Publication date: '+ article.pub_date;
    artlist.appendChild(date);
    var link = document.createElement('dd');
    var url = document.createElement('a');
    url.href = article.web_url;
    url.innerText = 'Link';
    link.appendChild(url);
    artlist.appendChild(link);


  });

}
