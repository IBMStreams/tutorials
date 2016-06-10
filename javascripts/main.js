
$(document).ready(function(){
  var h1h2 = $("h1, h2")
  var links = $("a")
  var sidebar = $("ul.nav-sidebar");
 h1h2.each(function(){
	var sidebar = $("ul.nav-sidebar");
    sidebar.append("<li class='tag-" + this.nodeName.toLowerCase() + "'><a class='toc' href='#" + $(this).text().toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g,'') + "'> " + $(this).text() + "</a></li>");
  /*   sidebar.append("<li class='tag-h1'><a class='toc' href='" + location.origin + "/tutorials/docs/spl-lab/Lab-3/'>Lab 3</a></li>"); */
//This is Where I tested adding a link, use as template
    $(this).attr("id",$(this).text().toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g,''));
  });
/*links.each(function(){
    potential use of links function
}*/
});