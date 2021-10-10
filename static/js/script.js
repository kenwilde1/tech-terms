$("form[name=register-form").submit(function(e) {
    e.preventDefault();
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/register",
      type: "POST",
      data: data,
      dataType: "json",
      success: (resp) => {
          window.location.href = '/dashboard/'
      },
      error: (resp) => {
          $error.text(resp.responseJSON.error)
      }
    });
  });

$("form[name=login-form").submit(function(e) {
    e.preventDefault();
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/login",
      type: "POST",
      data: data,
      dataType: "json",
      success: (resp) => {
          window.location.href = '/dashboard/'
      },
      error: (resp) => {
          $error.text(resp.responseJSON.error)
      }
    });
});

$("form[name=search-form").submit(function(e) {
  e.preventDefault();
  var $form = $(this);
  var $term = $form.find('#term')
  var $error = $form.find(".error");
  var $termDiv = $('body').find('.term-def');


  $.ajax({
    url: `/search/${$term.val()}`,
    type: "GET",
    dataType: "json",
    success: (resp) => {
      console.log('success:', resp)
        $termDiv.text(resp)
    },
    error: (resp) => {
        $error.text(resp.responseJSON.error)
        $termDiv.text('')
    }
  });
});

$("form[name=create-term-form").submit(function(e) {
  e.preventDefault();
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/create",
    type: "POST",
    data: data,
    dataType: "json",
    success: (resp) => {
        console.log(resp)
    },
    error: (resp) => {
        $error.text(resp.responseJSON.error)
    }
  });
});

$("#create-term-modal").click(function(e) {
  $('body').find('.modal').addClass('is-active');

  $(".modal-close").click(function(e) {
    $('body').find('.modal').removeClass('is-active');
  });

  $(".modal-background").click(function(e) {
    $('body').find('.modal').removeClass('is-active');
  });

  // $(".create-button").click(function(e) {
  //   $('body').find('.modal').removeClass('is-active');
  // });
});