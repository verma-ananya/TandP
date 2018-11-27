
//jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Add slideDown animation to dropdown
if ($(window).width() > 960) 
{
    // do something for big screens

    $('.navbar .dropdown').hover(function() {
    $(this).find('.dropdown-menu').first().stop(true, true).delay(150).slideDown();
    }, function() {
    $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideUp()
    });


    // $('.dropdown').on('show.bs.dropdown', function(e){
    //   $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    // });

    // // Add slideUp animation to dropdown
    // $('.dropdown').on('hide.bs.dropdown', function(e){
    //   $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    // });

    //jQuery to collapse the navbar on scroll
    $(window).scroll(function() {
        if ($(".navbar").offset().top > 170) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
            $("#logocdc").css({ "margin-top":"10px"});
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
            $("#logocdc").css({ "margin-top":"0px"});
        }
    });

    //triger click when hovering to have the drop down menu open
    // $('.dropdown').hover(function(){ 
    //     $('.dropdown-toggle', this).trigger('click'); 
    // });
}

// $(function(){
//     $(".dropdown-menu > li > a.trigger").on("click",function(e){
//         var current=$(this).next();
//         var grandparent=$(this).parent().parent();
//         if($(this).hasClass('right-caret')||$(this).hasClass('right-caret'))
//             $(this).toggleClass('right-caret right-caret');
//         grandparent.find('.right-caret').not(this).toggleClass('right-caret right-caret');
//         grandparent.find(".sub-menu:visible").not(current).hide();
//         current.toggle();
//         e.stopPropagation();
//     });
//     $(".dropdown-menu > li > a:not(.trigger)").on("click",function(){
//         var root=$(this).closest('.dropdown');
//         root.find('.right-caret').toggleClass('right-caret right-caret');
//         root.find('.sub-menu:visible').hide();
//     });
// });
if ($(window).width() > 768) 
{

}

