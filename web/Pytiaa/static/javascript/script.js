
  $('.slideshow').hide();
  var id = 0;
  var div = 0;
  var end = false;
  var play = false;
  $("#"+div).show();
  $("#"+div).children("div").hide();
  $('#'+div+' > .'+id).show();
  $("#go").click(function(){
    play = true;
    $("#go").hide();
    //$(".slideshow > div:gt(0)").hide();
    $('.slideshow').hide();
    $("#"+div).show();
    setInterval(function() {
      if($("#"+div).children("div").length>id && play){
        $('#'+div+' > .'+(id-1)).hide();
        $('#'+div+' > .'+id).show();
        id++;
      }
    },  400);
  });

  function check(){
    if(div==$("body").children(".slideshow").length-1){
      $("#next").hide();
    }else{
      $("#next").show();
    }
    if(div==0){
      $("#prev").hide();
    }else{
      $('#prev').show();
    }
  }

  check();

  $("#next").click(function(){
    div++;
    play = false;
    id = 0;
    $("#go").show();
    $('.slideshow').hide();
    $("#"+div).show();
    check();
  });
  $("#prev").click(function(){
    div--;
    play = false;
    id = 0;
    $("#go").show();
    $('.slideshow').hide();
    $("#"+div).show();
    check();
  });
