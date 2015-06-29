jQuery(document).ready(function(){
    /* improve this function for manipulation elements not using DOM tree*/
    $('#dropdown_blog').append('<div id="dropdown_div"></div>');

    $('#dropdown_div').hide().append('<ul id="dropdown_list"></ul>');

    $blog_dropdown_list = $('ul#dropdown_list');
    
    for (var name in categories) {
        if (categories.hasOwnProperty(name)) {

            $blog_dropdown_list.append('<li><a href="category/' + categories[name] + '">' + name + '</a></li>');

        }
    };
    
    $('#dropdown_blog').hover(function(){
        console.log('in')
        $('#dropdown_div').fadeIn()
        
    }, function(){
        $('#dropdown_div').fadeOut()
        console.log('out')
    });



});