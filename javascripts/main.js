
$(document).ready(function(){
  var h1h2 = $("h1, h2")
 h1h2.each(function(){
	var sidebar = $("ul.nav-sidebar");
    sidebar.append("<li class='tag-" + this.nodeName.toLowerCase() + "'><a class='toc' href='#" + $(this).text().toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g,'') + "'> " + $(this).text() + "</a></li>");
    $(this).attr("id",$(this).text().toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g,''));
  });
});
